# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .tunnel_param import TunnelParam
from ..custom_hostnames.bundle_method import BundleMethod

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

    bundle_method: BundleMethod
    """
    A ubiquitous bundle has the highest probability of being verified everywhere,
    even by clients using outdated or unusual trust stores. An optimal bundle uses
    the shortest chain and newest intermediates. And the force bundle verifies the
    chain, but does not otherwise modify it.
    """

    name: str
    """The keyless SSL name."""

    tunnel: TunnelParam
    """Configuration for using Keyless SSL through a Cloudflare Tunnel"""
