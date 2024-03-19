# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    account_id: Required[object]

    gateway_proxy_enabled: bool
    """Enable gateway proxy filtering on TCP."""

    gateway_udp_proxy_enabled: bool
    """Enable gateway proxy filtering on UDP."""

    root_certificate_installation_enabled: bool
    """Enable installation of cloudflare managed root certificate."""

    use_zt_virtual_ip: bool
    """Enable using CGNAT virtual IPv4."""
