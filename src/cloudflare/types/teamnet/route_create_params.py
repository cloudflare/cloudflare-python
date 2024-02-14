# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["RouteCreateParams"]


class RouteCreateParams(TypedDict, total=False):
    ip_network: Required[str]
    """The private IPv4 or IPv6 range connected by the route, in CIDR notation."""

    comment: str
    """Optional remark describing the route."""

    virtual_network_id: object
    """UUID of the Tunnel Virtual Network this route belongs to.

    If no virtual networks are configured, the route is assigned to the default
    virtual network of the account.
    """
