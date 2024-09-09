# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TunnelParam"]


class TunnelParam(TypedDict, total=False):
    private_ip: Required[str]
    """Private IP of the Key Server Host"""

    vnet_id: Required[str]
    """Cloudflare Tunnel Virtual Network ID"""
