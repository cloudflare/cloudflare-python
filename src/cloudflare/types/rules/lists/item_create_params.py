# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ..hostname_param import HostnameParam
from ..redirect_param import RedirectParam

__all__ = ["ItemCreateParams", "Body", "BodyUnionMember0", "BodyUnionMember1", "BodyUnionMember2", "BodyUnionMember3"]


class ItemCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account ID for this resource."""

    body: Required[Iterable[Body]]


class BodyUnionMember0(TypedDict, total=False):
    ip: Required[str]
    """An IPv4 address, an IPv4 CIDR, an IPv6 address, or an IPv6 CIDR."""

    comment: str
    """Defines an informative summary of the list item."""


class BodyUnionMember1(TypedDict, total=False):
    redirect: Required[RedirectParam]
    """The definition of the redirect."""

    comment: str
    """Defines an informative summary of the list item."""


class BodyUnionMember2(TypedDict, total=False):
    hostname: Required[HostnameParam]
    """
    Valid characters for hostnames are ASCII(7) letters from a to z, the digits from
    0 to 9, wildcards (\\**), and the hyphen (-).
    """

    comment: str
    """Defines an informative summary of the list item."""


class BodyUnionMember3(TypedDict, total=False):
    asn: Required[int]
    """Defines a non-negative 32 bit integer."""

    comment: str
    """Defines an informative summary of the list item."""


Body: TypeAlias = Union[BodyUnionMember0, BodyUnionMember1, BodyUnionMember2, BodyUnionMember3]
