# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OnRampCreateParams"]


class OnRampCreateParams(TypedDict, total=False):
    account_id: Required[str]

    cloud_type: Required[Literal["AWS", "AZURE", "GOOGLE"]]

    install_routes_in_cloud: Required[bool]

    install_routes_in_magic_wan: Required[bool]

    name: Required[str]

    type: Required[Literal["OnrampTypeSingle", "OnrampTypeHub"]]

    adopted_hub_id: str

    attached_hubs: List[str]

    attached_vpcs: List[str]

    description: str

    hub_provider_id: str

    manage_hub_to_hub_attachments: bool

    manage_vpc_to_hub_attachments: bool

    region: str

    vpc: str

    forwarded: str
