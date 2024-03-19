# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .policies import TeamsDevicesSplitTunnel, TeamsDevicesFallbackDomain, TeamsDevicesSplitTunnelInclude
from ...._models import BaseModel

__all__ = ["TeamsDevicesDeviceSettingsPolicy", "ServiceModeV2"]


class ServiceModeV2(BaseModel):
    mode: Optional[str] = None
    """The mode to run the WARP client under."""

    port: Optional[float] = None
    """The port number when used with proxy mode."""


class TeamsDevicesDeviceSettingsPolicy(BaseModel):
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
    """Whether the policy is the default policy for an account."""

    description: Optional[str] = None
    """A description of the policy."""

    disable_auto_fallback: Optional[bool] = None
    """
    If the `dns_server` field of a fallback domain is not present, the client will
    fall back to a best guess of the default/system DNS resolvers unless this policy
    option is set to `true`.
    """

    enabled: Optional[bool] = None
    """Whether the policy will be applied to matching devices."""

    exclude: Optional[List[TeamsDevicesSplitTunnel]] = None

    exclude_office_ips: Optional[bool] = None
    """Whether to add Microsoft IPs to Split Tunnel exclusions."""

    fallback_domains: Optional[List[TeamsDevicesFallbackDomain]] = None

    gateway_unique_id: Optional[str] = None

    include: Optional[List[TeamsDevicesSplitTunnelInclude]] = None

    lan_allow_minutes: Optional[float] = None
    """The amount of time in minutes a user is allowed access to their LAN.

    A value of 0 will allow LAN access until the next WARP reconnection, such as a
    reboot or a laptop waking from sleep. Note that this field is omitted from the
    response if null or unset.
    """

    lan_allow_subnet_size: Optional[float] = None
    """The size of the subnet for the local access network.

    Note that this field is omitted from the response if null or unset.
    """

    match: Optional[str] = None
    """The wirefilter expression to match devices."""

    name: Optional[str] = None
    """The name of the device settings profile."""

    policy_id: Optional[str] = None
    """Device ID."""

    precedence: Optional[float] = None
    """The precedence of the policy.

    Lower values indicate higher precedence. Policies will be evaluated in ascending
    order of this field.
    """

    service_mode_v2: Optional[ServiceModeV2] = None

    support_url: Optional[str] = None
    """The URL to launch when the Send Feedback button is clicked."""

    switch_locked: Optional[bool] = None
    """
    Whether to allow the user to turn off the WARP switch and disconnect the client.
    """
