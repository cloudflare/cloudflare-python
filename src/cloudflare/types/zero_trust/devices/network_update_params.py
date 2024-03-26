# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NetworkUpdateParams", "Config"]


class NetworkUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    config: Config
    """
    The configuration object containing information for the WARP client to detect
    the managed network.
    """

    name: str
    """The name of the device managed network. This name must be unique."""

    type: Literal["tls"]
    """The type of device managed network."""


class Config(TypedDict, total=False):
    tls_sockaddr: Required[str]
    """
    A network address of the form "host:port" that the WARP client will use to
    detect the presence of a TLS host.
    """

    sha256: str
    """
    The SHA-256 hash of the TLS certificate presented by the host found at
    tls_sockaddr. If absent, regular certificate verification (trusted roots, valid
    timestamp, etc) will be used to validate the certificate.
    """
