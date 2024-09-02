# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DeviceSettings"]


class DeviceSettings(BaseModel):
    disable_for_time: Optional[float] = None
    """
    Sets the time limit, in seconds, that a user can use an override code to bypass
    WARP.
    """

    gateway_proxy_enabled: Optional[bool] = None
    """Enable gateway proxy filtering on TCP."""

    gateway_udp_proxy_enabled: Optional[bool] = None
    """Enable gateway proxy filtering on UDP."""

    root_certificate_installation_enabled: Optional[bool] = None
    """Enable installation of cloudflare managed root certificate."""

    use_zt_virtual_ip: Optional[bool] = None
    """Enable using CGNAT virtual IPv4."""
