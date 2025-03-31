# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .tunnel_param import TunnelParam

__all__ = ["KeylessCertificateCreateParams"]


class KeylessCertificateCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    certificate: Required[str]
    """The zone's SSL certificate or SSL certificate and intermediate(s)."""

    host: Required[str]
    """The keyless SSL name."""

    port: Required[float]
    """
    The keyless SSL port used to communicate between Cloudflare and the client's
    Keyless SSL server.
    """

    bundle_method: object

    name: str
    """The keyless SSL name."""

    tunnel: TunnelParam
    """Configuration for using Keyless SSL through a Cloudflare Tunnel"""
