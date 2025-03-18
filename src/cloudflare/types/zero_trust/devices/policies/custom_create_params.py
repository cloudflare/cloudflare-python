# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..split_tunnel_exclude_param import SplitTunnelExcludeParam

__all__ = ["CustomCreateParams", "ServiceModeV2"]


class CustomCreateParams(TypedDict, total=False):
    account_id: Required[str]

    match: Required[str]
    """The wirefilter expression to match devices."""

    name: Required[str]
    """The name of the device settings profile."""

    precedence: Required[float]
    """The precedence of the policy.

    Lower values indicate higher precedence. Policies will be evaluated in ascending
    order of this field.
    """

    allow_mode_switch: bool
    """Whether to allow the user to switch WARP between modes."""

    allow_updates: bool
    """
    Whether to receive update notifications when a new version of the client is
    available.
    """

    allowed_to_leave: bool
    """Whether to allow devices to leave the organization."""

    auto_connect: float
    """The amount of time in seconds to reconnect after having been disabled."""

    captive_portal: float
    """Turn on the captive portal after the specified amount of time."""

    description: str
    """A description of the policy."""

    disable_auto_fallback: bool
    """
    If the `dns_server` field of a fallback domain is not present, the client will
    fall back to a best guess of the default/system DNS resolvers unless this policy
    option is set to `true`.
    """

    enabled: bool
    """Whether the policy will be applied to matching devices."""

    exclude: Iterable[SplitTunnelExcludeParam]
    """List of routes excluded in the WARP client's tunnel.

    Both 'exclude' and 'include' cannot be set in the same request.
    """

    exclude_office_ips: bool
    """Whether to add Microsoft IPs to Split Tunnel exclusions."""

    include: Iterable[SplitTunnelExcludeParam]
    """List of routes included in the WARP client's tunnel.

    Both 'exclude' and 'include' cannot be set in the same request.
    """

    lan_allow_minutes: float
    """The amount of time in minutes a user is allowed access to their LAN.

    A value of 0 will allow LAN access until the next WARP reconnection, such as a
    reboot or a laptop waking from sleep. Note that this field is omitted from the
    response if null or unset.
    """

    lan_allow_subnet_size: float
    """The size of the subnet for the local access network.

    Note that this field is omitted from the response if null or unset.
    """

    register_interface_ip_with_dns: bool
    """
    Determines if the operating system will register WARP's local interface IP with
    your on-premises DNS server.
    """

    service_mode_v2: ServiceModeV2

    support_url: str
    """The URL to launch when the Send Feedback button is clicked."""

    switch_locked: bool
    """
    Whether to allow the user to turn off the WARP switch and disconnect the client.
    """

    tunnel_protocol: str
    """Determines which tunnel protocol to use."""


class ServiceModeV2(TypedDict, total=False):
    mode: str
    """The mode to run the WARP client under."""

    port: float
    """The port number when used with proxy mode."""
