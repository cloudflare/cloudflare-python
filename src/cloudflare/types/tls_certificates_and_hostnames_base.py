# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TLSCertificatesAndHostnamesBase", "Tunnel"]


class Tunnel(BaseModel):
    private_ip: str
    """Private IP of the Key Server Host"""

    vnet_id: str
    """Cloudflare Tunnel Virtual Network ID"""


class TLSCertificatesAndHostnamesBase(BaseModel):
    id: str
    """Keyless certificate identifier tag."""

    created_on: datetime
    """When the Keyless SSL was created."""

    enabled: bool
    """Whether or not the Keyless SSL is on or off."""

    host: str
    """The keyless SSL name."""

    modified_on: datetime
    """When the Keyless SSL was last modified."""

    name: str
    """The keyless SSL name."""

    permissions: List[object]
    """
    Available permissions for the Keyless SSL for the current user requesting the
    item.
    """

    port: float
    """
    The keyless SSL port used to communicate between Cloudflare and the client's
    Keyless SSL server.
    """

    status: Literal["active", "deleted"]
    """Status of the Keyless SSL."""

    tunnel: Optional[Tunnel] = None
    """Configuration for using Keyless SSL through a Cloudflare Tunnel"""
