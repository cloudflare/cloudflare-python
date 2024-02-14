# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["NetworkDeleteParams"]


class NetworkDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    tun_type: Literal["cfd_tunnel", "warp_connector", "ip_sec", "gre", "cni"]
    """The type of tunnel."""
