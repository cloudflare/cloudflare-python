# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TunnelVirtualNetwork"]


class TunnelVirtualNetwork(BaseModel):
    id: str
    """UUID of the virtual network."""

    comment: str
    """Optional remark describing the virtual network."""

    created_at: object
    """Timestamp of when the virtual network was created."""

    is_default_network: bool
    """If `true`, this virtual network is the default for the account."""

    name: str
    """A user-friendly name for the virtual network."""

    deleted_at: Optional[object] = None
    """Timestamp of when the virtual network was deleted.

    If `null`, the virtual network has not been deleted.
    """
