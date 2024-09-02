# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["VirtualNetworkListParams"]


class VirtualNetworkListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    id: str
    """UUID of the virtual network."""

    is_default: bool
    """If `true`, only include the default virtual network.

    If `false`, exclude the default virtual network. If empty, all virtual networks
    will be included.
    """

    is_deleted: bool
    """If `true`, only include deleted virtual networks.

    If `false`, exclude deleted virtual networks. If empty, all virtual networks
    will be included.
    """

    name: str
    """A user-friendly name for the virtual network."""
