# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SettingEditParams"]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]

    disable_for_time: float
    """
    Sets the time limit, in seconds, that a user can use an override code to bypass
    WARP.
    """

    external_emergency_signal_enabled: bool
    """Controls whether the external emergency disconnect feature is enabled."""

    external_emergency_signal_fingerprint: str
    """
    The SHA256 fingerprint (64 hexadecimal characters) of the HTTPS server
    certificate for the external_emergency_signal_url. If provided, the WARP client
    will use this value to verify the server's identity. The device will ignore any
    response if the server's certificate fingerprint does not exactly match this
    value.
    """

    external_emergency_signal_interval: str
    """
    The interval at which the WARP client fetches the emergency disconnect signal,
    formatted as a duration string (e.g., "5m", "2m30s", "1h"). Minimum 30 seconds.
    """

    external_emergency_signal_url: str
    """The HTTPS URL from which to fetch the emergency disconnect signal.

    Must use HTTPS and have an IPv4 or IPv6 address as the host.
    """

    gateway_proxy_enabled: bool
    """Enable gateway proxy filtering on TCP."""

    gateway_udp_proxy_enabled: bool
    """Enable gateway proxy filtering on UDP."""

    root_certificate_installation_enabled: bool
    """Enable installation of cloudflare managed root certificate."""

    use_zt_virtual_ip: bool
    """Enable using CGNAT virtual IPv4."""
