# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["InterconnectCreateParams", "NscInterconnectCreatePhysicalBody", "NscInterconnectCreateGcpPartnerBody"]


class NscInterconnectCreatePhysicalBody(TypedDict, total=False):
    account_id: Required[str]
    """Customer account tag"""

    account: Required[str]

    slot_id: Required[str]

    type: Required[str]

    speed: Optional[str]


class NscInterconnectCreateGcpPartnerBody(TypedDict, total=False):
    account_id: Required[str]
    """Customer account tag"""

    account: Required[str]

    bandwidth: Required[Literal["50M", "100M", "200M", "300M", "400M", "500M", "1G", "2G", "5G", "10G", "20G", "50G"]]
    """Bandwidth structure as visible through the customer-facing API."""

    pairing_key: Required[str]
    """Pairing key provided by GCP"""

    type: Required[str]


InterconnectCreateParams: TypeAlias = Union[NscInterconnectCreatePhysicalBody, NscInterconnectCreateGcpPartnerBody]
