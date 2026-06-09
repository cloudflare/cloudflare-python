# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = [
    "ConfigurationGetResponse",
    "Config",
    "ConfigTunnelMeshAwsConfig",
    "ConfigTunnelMeshLocalConfig",
    "ConfigTunnelMeshLocalConfigVip",
    "ConfigTunnelMeshLocalConfigVipsPrevious",
]


class ConfigTunnelMeshAwsConfig(BaseModel):
    fnr_id: str
    """
    Floating Network Resource ID — the secondary ENI that is moved between nodes on
    failover.
    """


class ConfigTunnelMeshLocalConfigVip(BaseModel):
    address: str
    """Virtual IP address (IPv4 or IPv6)."""


class ConfigTunnelMeshLocalConfigVipsPrevious(BaseModel):
    address: str
    """Virtual IP address (IPv4 or IPv6)."""


class ConfigTunnelMeshLocalConfig(BaseModel):
    vips: List[ConfigTunnelMeshLocalConfigVip]
    """VIPs to assign on the CloudflareWARP interface."""

    vips_previous: Optional[List[ConfigTunnelMeshLocalConfigVipsPrevious]] = None
    """VIPs to clean up on demotion or version drift."""


Config: TypeAlias = Union[ConfigTunnelMeshAwsConfig, ConfigTunnelMeshLocalConfig, None]


class ConfigurationGetResponse(BaseModel):
    configuration_version: int
    """Monotonically increasing configuration version, incremented on each PUT."""

    created_at: datetime
    """Timestamp of when the resource was created."""

    ha_mode: Literal["none", "disabled", "aws", "local"]
    """High-availability mode for the WARP Connector tunnel.

    `none` means HA is enabled but no provider is configured yet (newly created
    tunnels default to this). `disabled` means HA is explicitly turned off. `aws`
    uses AWS ENI move for failover. `local` uses virtual IPs (VIPs) on the local
    interface.
    """

    tunnel_id: str
    """UUID of the tunnel."""

    config: Optional[Config] = None
    """Provider-specific configuration. Present for `aws` and `local` modes."""

    updated_at: Optional[datetime] = None
    """Timestamp of the last update. Null if never updated."""
