# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DeviceNetwork"]


class DeviceNetwork(BaseModel):
    config: Optional[object] = None
    """
    The configuration object containing information for the WARP client to detect
    the managed network.
    """

    name: Optional[str] = None
    """The name of the device managed network. This name must be unique."""

    network_id: Optional[str] = None
    """API UUID."""

    type: Optional[Literal["tls"]] = None
    """The type of device managed network."""
