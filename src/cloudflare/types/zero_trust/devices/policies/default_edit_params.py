# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..split_tunnel_exclude_param import SplitTunnelExcludeParam

__all__ = ["DefaultEditParams", "ServiceModeV2"]


class DefaultEditParams(TypedDict, total=False):
    account_id: Required[str]

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

    disable_auto_fallback: bool
    """
    If the `dns_server` field of a fallback domain is not present, the client will
    fall back to a best guess of the default/system DNS resolvers unless this policy
    option is set to `true`.
    """

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
