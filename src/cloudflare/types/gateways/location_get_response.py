# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["LocationGetResponse", "Network"]


class Network(BaseModel):
    network: str
    """The IPv4 address or IPv4 CIDR. IPv4 CIDRs are limited to a maximum of /24."""


class LocationGetResponse(BaseModel):
    id: Optional[object] = None

    client_default: Optional[bool] = None
    """True if the location is the default location."""

    created_at: Optional[datetime] = None

    doh_subdomain: Optional[str] = None
    """The DNS over HTTPS domain to send DNS requests to.

    This field is auto-generated by Gateway.
    """

    ecs_support: Optional[bool] = None
    """True if the location needs to resolve EDNS queries."""

    ip: Optional[str] = None
    """IPV6 destination ip assigned to this location.

    DNS requests sent to this IP will counted as the request under this location.
    This field is auto-generated by Gateway.
    """

    name: Optional[str] = None
    """The name of the location."""

    networks: Optional[List[Network]] = None
    """A list of network ranges that requests from this location would originate from."""

    updated_at: Optional[datetime] = None
