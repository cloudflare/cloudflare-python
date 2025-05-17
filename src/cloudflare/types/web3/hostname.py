# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Hostname"]


class Hostname(BaseModel):
    id: Optional[str] = None
    """Specify the identifier of the hostname."""

    created_on: Optional[datetime] = None

    description: Optional[str] = None
    """Specify an optional description of the hostname."""

    dnslink: Optional[str] = None
    """Specify the DNSLink value used if the target is ipfs."""

    modified_on: Optional[datetime] = None

    name: Optional[str] = None
    """Specify the hostname that points to the target gateway via CNAME."""

    status: Optional[Literal["active", "pending", "deleting", "error"]] = None
    """Specifies the status of the hostname's activation."""

    target: Optional[Literal["ethereum", "ipfs", "ipfs_universal_path"]] = None
    """Specify the target gateway of the hostname."""
