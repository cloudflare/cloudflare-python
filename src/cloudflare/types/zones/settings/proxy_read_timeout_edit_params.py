# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .zone_setting_proxy_read_timeout_param import ZoneSettingProxyReadTimeoutParam

__all__ = ["ProxyReadTimeoutEditParams"]


class ProxyReadTimeoutEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[ZoneSettingProxyReadTimeoutParam]
    """Maximum time between two read operations from origin."""
