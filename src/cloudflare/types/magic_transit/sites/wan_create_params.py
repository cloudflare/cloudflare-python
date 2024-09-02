# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from .wan_static_addressing_param import WANStaticAddressingParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["WANCreateParams"]


class WANCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    physport: Required[int]

    vlan_tag: Required[int]
    """VLAN port number."""

    name: str

    priority: int

    static_addressing: WANStaticAddressingParam
    """(optional) if omitted, use DHCP.

    Submit secondary_address when site is in high availability mode.
    """
