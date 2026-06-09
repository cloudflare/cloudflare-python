# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ConfigurationUpdateParams",
    "Config",
    "ConfigTunnelMeshAwsConfig",
    "ConfigTunnelMeshLocalConfig",
    "ConfigTunnelMeshLocalConfigVip",
    "ConfigTunnelMeshLocalConfigVipsPrevious",
]


class ConfigurationUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    ha_mode: Required[Literal["none", "disabled", "aws", "local"]]
    """High-availability mode for the WARP Connector tunnel.

    `none` means HA is enabled but no provider is configured yet (newly created
    tunnels default to this). `disabled` means HA is explicitly turned off. `aws`
    uses AWS ENI move for failover. `local` uses virtual IPs (VIPs) on the local
    interface.
    """

    config: Optional[Config]
    """Provider-specific configuration.

    Required shape depends on ha_mode. For `aws`, must contain `fnr_id`. For
    `local`, must contain `vips`. For `none` and `disabled`, must be empty or
    omitted.
    """


class ConfigTunnelMeshAwsConfig(TypedDict, total=False):
    fnr_id: Required[str]
    """
    Floating Network Resource ID — the secondary ENI that is moved between nodes on
    failover.
    """


class ConfigTunnelMeshLocalConfigVip(TypedDict, total=False):
    address: Required[str]
    """Virtual IP address (IPv4 or IPv6)."""


class ConfigTunnelMeshLocalConfigVipsPrevious(TypedDict, total=False):
    address: Required[str]
    """Virtual IP address (IPv4 or IPv6)."""


class ConfigTunnelMeshLocalConfig(TypedDict, total=False):
    vips: Required[Iterable[ConfigTunnelMeshLocalConfigVip]]
    """VIPs to assign on the CloudflareWARP interface."""

    vips_previous: Iterable[ConfigTunnelMeshLocalConfigVipsPrevious]
    """VIPs to clean up on demotion or version drift."""


Config: TypeAlias = Union[ConfigTunnelMeshAwsConfig, ConfigTunnelMeshLocalConfig, object]
