# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["OnRampEditParams"]


class OnRampEditParams(TypedDict, total=False):
    account_id: Required[str]

    attached_hubs: SequenceNotStr[str]

    attached_vpcs: SequenceNotStr[str]

    description: str

    install_routes_in_cloud: bool

    install_routes_in_magic_wan: bool

    manage_hub_to_hub_attachments: bool

    manage_vpc_to_hub_attachments: bool

    name: str

    vpc: str
