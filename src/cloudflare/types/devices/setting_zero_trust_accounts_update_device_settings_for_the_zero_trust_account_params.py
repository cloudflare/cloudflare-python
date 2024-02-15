# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountParams"]


class SettingZeroTrustAccountsUpdateDeviceSettingsForTheZeroTrustAccountParams(TypedDict, total=False):
    gateway_proxy_enabled: bool
    """Enable gateway proxy filtering on TCP."""

    gateway_udp_proxy_enabled: bool
    """Enable gateway proxy filtering on UDP."""

    root_certificate_installation_enabled: bool
    """Enable installation of cloudflare managed root certificate."""

    use_zt_virtual_ip: bool
    """Enable using CGNAT virtual IPv4."""
