# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["EdgeIPs", "UnionMember0", "UnionMember1"]


class UnionMember0(BaseModel):
    connectivity: Optional[Literal["all", "ipv4", "ipv6"]] = None
    """The IP versions supported for inbound connections on Spectrum anycast IPs."""

    type: Optional[Literal["dynamic"]] = None
    """The type of edge IP configuration specified.

    Dynamically allocated edge IPs use Spectrum anycast IPs in accordance with the
    connectivity you specify. Only valid with CNAME DNS names.
    """


class UnionMember1(BaseModel):
    ips: Optional[List[str]] = None
    """
    The array of customer owned IPs we broadcast via anycast for this hostname and
    application.
    """

    type: Optional[Literal["static"]] = None
    """The type of edge IP configuration specified.

    Statically allocated edge IPs use customer IPs in accordance with the ips array
    you specify. Only valid with ADDRESS DNS names.
    """


EdgeIPs: TypeAlias = Union[UnionMember0, UnionMember1]
