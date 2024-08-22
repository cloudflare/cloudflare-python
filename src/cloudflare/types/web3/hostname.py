# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Hostname"]


class Hostname(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    created_on: Optional[datetime] = None

    description: Optional[str] = None
    """An optional description of the hostname."""

    dnslink: Optional[str] = None
    """DNSLink value used if the target is ipfs."""

    modified_on: Optional[datetime] = None

    name: Optional[str] = None
    """The hostname that will point to the target gateway via CNAME."""

    status: Optional[Literal["active", "pending", "deleting", "error"]] = None
    """Status of the hostname's activation."""

    target: Optional[Literal["ethereum", "ipfs", "ipfs_universal_path"]] = None
    """Target gateway of the hostname."""
