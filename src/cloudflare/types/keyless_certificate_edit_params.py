# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KeylessCertificateEditParams", "Tunnel"]


class KeylessCertificateEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    enabled: bool
    """Whether or not the Keyless SSL is on or off."""

    host: str
    """The keyless SSL name."""

    name: str
    """The keyless SSL name."""

    port: float
    """
    The keyless SSL port used to communicate between Cloudflare and the client's
    Keyless SSL server.
    """

    tunnel: Tunnel
    """Configuration for using Keyless SSL through a Cloudflare Tunnel"""


class Tunnel(TypedDict, total=False):
    private_ip: Required[str]
    """Private IP of the Key Server Host"""

    vnet_id: Required[str]
    """Cloudflare Tunnel Virtual Network ID"""
