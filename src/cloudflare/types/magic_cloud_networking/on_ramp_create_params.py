# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["OnRampCreateParams"]


class OnRampCreateParams(TypedDict, total=False):
    account_id: str

    cloud_type: Required[Literal["AWS", "AZURE", "GOOGLE"]]

    dynamic_routing: Required[bool]
    """Enables BGP routing.

    When enabling this feature, set both install_routes_in_cloud and
    install_routes_in_magic_wan to false.
    """

    install_routes_in_cloud: Required[bool]

    install_routes_in_magic_wan: Required[bool]

    name: Required[str]

    type: Required[Literal["OnrampTypeSingle", "OnrampTypeHub"]]

    adopted_hub_id: str

    attached_hubs: SequenceNotStr[str]

    attached_vpcs: SequenceNotStr[str]

    cloud_asn: int
    """Sets the cloud-side ASN.

    If unset or zero, the cloud's default ASN takes effect.
    """

    description: str

    hub_provider_id: str

    manage_hub_to_hub_attachments: bool

    manage_vpc_to_hub_attachments: bool

    region: str

    vpc: str

    forwarded: str
