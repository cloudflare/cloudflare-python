# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PolicyEditParams", "ServiceModeV2"]


class PolicyEditParams(TypedDict, total=False):
    account_id: Required[object]

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
    """The amount of time in minutes to reconnect after having been disabled."""

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

    exclude_office_ips: bool
    """Whether to add Microsoft IPs to Split Tunnel exclusions."""

    match: str
    """The wirefilter expression to match devices."""

    name: str
    """The name of the device settings profile."""

    precedence: float
    """The precedence of the policy.

    Lower values indicate higher precedence. Policies will be evaluated in ascending
    order of this field.
    """

    service_mode_v2: ServiceModeV2

    support_url: str
    """The URL to launch when the Send Feedback button is clicked."""

    switch_locked: bool
    """
    Whether to allow the user to turn off the WARP switch and disconnect the client.
    """


class ServiceModeV2(TypedDict, total=False):
    mode: str
    """The mode to run the WARP client under."""

    port: float
    """The port number when used with proxy mode."""
