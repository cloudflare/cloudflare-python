# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectivitySettingEditParams"]


class ConnectivitySettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    icmp_proxy_enabled: bool
    """A flag to enable the ICMP proxy for the account network."""

    offramp_warp_enabled: bool
    """A flag to enable WARP to WARP traffic."""
