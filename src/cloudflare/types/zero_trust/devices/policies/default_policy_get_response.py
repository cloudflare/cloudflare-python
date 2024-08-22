# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional, List

from .split_tunnel_exclude import SplitTunnelExclude

from .fallback_domain import FallbackDomain

from .split_tunnel_include import SplitTunnelInclude

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DefaultPolicyGetResponse", "ServiceModeV2"]

class ServiceModeV2(BaseModel):
    mode: Optional[str] = None
    """The mode to run the WARP client under."""

    port: Optional[float] = None
    """The port number when used with proxy mode."""

class DefaultPolicyGetResponse(BaseModel):
    allow_mode_switch: Optional[bool] = None
    """Whether to allow the user to switch WARP between modes."""

    allow_updates: Optional[bool] = None
    """
    Whether to receive update notifications when a new version of the client is
    available.
    """

    allowed_to_leave: Optional[bool] = None
    """Whether to allow devices to leave the organization."""

    auto_connect: Optional[float] = None
    """The amount of time in minutes to reconnect after having been disabled."""

    captive_portal: Optional[float] = None
    """Turn on the captive portal after the specified amount of time."""

    default: Optional[bool] = None
    """Whether the policy will be applied to matching devices."""

    disable_auto_fallback: Optional[bool] = None
    """
    If the `dns_server` field of a fallback domain is not present, the client will
    fall back to a best guess of the default/system DNS resolvers unless this policy
    option is set to `true`.
    """

    enabled: Optional[bool] = None
    """Whether the policy will be applied to matching devices."""

    exclude: Optional[List[SplitTunnelExclude]] = None

    exclude_office_ips: Optional[bool] = None
    """Whether to add Microsoft IPs to Split Tunnel exclusions."""

    fallback_domains: Optional[List[FallbackDomain]] = None

    gateway_unique_id: Optional[str] = None

    include: Optional[List[SplitTunnelInclude]] = None

    service_mode_v2: Optional[ServiceModeV2] = None

    support_url: Optional[str] = None
    """The URL to launch when the Send Feedback button is clicked."""

    switch_locked: Optional[bool] = None
    """
    Whether to allow the user to turn off the WARP switch and disconnect the client.
    """

    tunnel_protocol: Optional[str] = None
    """Determines which tunnel protocol to use."""