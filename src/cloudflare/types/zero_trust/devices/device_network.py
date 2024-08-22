# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DeviceNetwork", "Config"]


class Config(BaseModel):
    tls_sockaddr: str
    """
    A network address of the form "host:port" that the WARP client will use to
    detect the presence of a TLS host.
    """

    sha256: Optional[str] = None
    """
    The SHA-256 hash of the TLS certificate presented by the host found at
    tls_sockaddr. If absent, regular certificate verification (trusted roots, valid
    timestamp, etc) will be used to validate the certificate.
    """


class DeviceNetwork(BaseModel):
    config: Optional[Config] = None
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
