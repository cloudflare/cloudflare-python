# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = ["EdgeIPsParam", "UnionMember0", "UnionMember1"]


class UnionMember0(TypedDict, total=False):
    connectivity: Literal["all", "ipv4", "ipv6"]
    """The IP versions supported for inbound connections on Spectrum anycast IPs."""

    type: Literal["dynamic"]
    """The type of edge IP configuration specified.

    Dynamically allocated edge IPs use Spectrum anycast IPs in accordance with the
    connectivity you specify. Only valid with CNAME DNS names.
    """


class UnionMember1(TypedDict, total=False):
    ips: List[str]
    """
    The array of customer owned IPs we broadcast via anycast for this hostname and
    application.
    """

    type: Literal["static"]
    """The type of edge IP configuration specified.

    Statically allocated edge IPs use customer IPs in accordance with the ips array
    you specify. Only valid with ADDRESS DNS names.
    """


EdgeIPsParam: TypeAlias = Union[UnionMember0, UnionMember1]
