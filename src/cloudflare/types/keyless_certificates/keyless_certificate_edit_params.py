# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .tunnel_param import TunnelParam

__all__ = ["KeylessCertificateEditParams"]


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

    tunnel: TunnelParam
    """Configuration for using Keyless SSL through a Cloudflare Tunnel"""
