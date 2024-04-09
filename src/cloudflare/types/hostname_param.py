# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .tunnel_param import TunnelParam

__all__ = ["HostnameParam"]


class HostnameParam(TypedDict, total=False):
    host: Required[str]
    """The keyless SSL name."""

    port: Required[float]
    """
    The keyless SSL port used to communicate between Cloudflare and the client's
    Keyless SSL server.
    """

    tunnel: TunnelParam
    """Configuration for using Keyless SSL through a Cloudflare Tunnel"""
