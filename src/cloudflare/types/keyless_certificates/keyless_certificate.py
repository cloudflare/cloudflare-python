# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .tunnel import Tunnel
from ..._models import BaseModel

__all__ = ["KeylessCertificate"]


class KeylessCertificate(BaseModel):
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

    permissions: List[str]
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
