# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["CloudflareSourceUpdateResponse"]


class CloudflareSourceUpdateResponse(BaseModel):
    id: Optional[str] = None
    """The UUID of the subnet."""

    comment: Optional[str] = None
    """An optional description of the subnet."""

    created_at: Optional[datetime] = None
    """Timestamp of when the resource was created."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the resource was deleted.

    If `null`, the resource has not been deleted.
    """

    is_default_network: Optional[bool] = None
    """If `true`, this is the default subnet for the account.

    There can only be one default subnet per account.
    """

    name: Optional[str] = None
    """A user-friendly name for the subnet."""

    network: Optional[str] = None
    """The private IPv4 or IPv6 range defining the subnet, in CIDR notation."""

    subnet_type: Optional[Literal["cloudflare_source"]] = None
    """The type of subnet."""
