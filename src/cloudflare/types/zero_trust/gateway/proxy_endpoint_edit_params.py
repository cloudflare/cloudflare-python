# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from .gateway_ips import GatewayIPs

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ProxyEndpointEditParams"]

class ProxyEndpointEditParams(TypedDict, total=False):
    account_id: Required[str]

    ips: List[GatewayIPs]
    """A list of CIDRs to restrict ingress connections."""

    name: str
    """The name of the proxy endpoint."""