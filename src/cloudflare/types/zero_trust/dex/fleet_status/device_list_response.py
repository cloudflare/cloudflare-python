# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "DeviceListResponse",
    "CPUPctByApp",
    "DeviceIPV4",
    "DeviceIPV4Location",
    "DeviceIPV6",
    "DeviceIPV6Location",
    "GatewayIPV4",
    "GatewayIPV4Location",
    "GatewayIPV6",
    "GatewayIPV6Location",
    "ISPIPV4",
    "ISPIPV4Location",
    "ISPIPV6",
    "ISPIPV6Location",
    "RamUsedPctByApp",
    "RTT",
    "RTTMinRTTUs",
    "RTTRTTUs",
    "RTTRTTVarUs",
    "TunnelStats",
    "TunnelStatsBytesLost",
    "TunnelStatsBytesReceived",
    "TunnelStatsBytesRetransmitted",
    "TunnelStatsBytesSent",
    "TunnelStatsPacketsLost",
    "TunnelStatsPacketsReceived",
    "TunnelStatsPacketsRetransmitted",
    "TunnelStatsPacketsSent",
]


class CPUPctByApp(BaseModel):
    cpu_pct: Optional[float] = None
    """CPU usage percentage, on a scale of 0 to 100."""

    name: Optional[str] = None
    """Application name."""


class DeviceIPV4Location(BaseModel):
    city: Optional[str] = None

    country_iso: Optional[str] = None

    state_iso: Optional[str] = None

    zip: Optional[str] = None


class DeviceIPV4(BaseModel):
    address: Optional[str] = None

    asn: Optional[int] = None

    aso: Optional[str] = None

    location: Optional[DeviceIPV4Location] = None

    name: Optional[str] = None

    netmask: Optional[str] = None

    version: Optional[int] = None
    """IP version (`1` for IPv4, `2` for IPv6, `0` if unknown)."""


class DeviceIPV6Location(BaseModel):
    city: Optional[str] = None

    country_iso: Optional[str] = None

    state_iso: Optional[str] = None

    zip: Optional[str] = None


class DeviceIPV6(BaseModel):
    address: Optional[str] = None

    asn: Optional[int] = None

    aso: Optional[str] = None

    location: Optional[DeviceIPV6Location] = None

    name: Optional[str] = None

    netmask: Optional[str] = None

    version: Optional[int] = None
    """IP version (`1` for IPv4, `2` for IPv6, `0` if unknown)."""


class GatewayIPV4Location(BaseModel):
    city: Optional[str] = None

    country_iso: Optional[str] = None

    state_iso: Optional[str] = None

    zip: Optional[str] = None


class GatewayIPV4(BaseModel):
    address: Optional[str] = None

    asn: Optional[int] = None

    aso: Optional[str] = None

    location: Optional[GatewayIPV4Location] = None

    name: Optional[str] = None

    netmask: Optional[str] = None

    version: Optional[int] = None
    """IP version (`1` for IPv4, `2` for IPv6, `0` if unknown)."""


class GatewayIPV6Location(BaseModel):
    city: Optional[str] = None

    country_iso: Optional[str] = None

    state_iso: Optional[str] = None

    zip: Optional[str] = None


class GatewayIPV6(BaseModel):
    address: Optional[str] = None

    asn: Optional[int] = None

    aso: Optional[str] = None

    location: Optional[GatewayIPV6Location] = None

    name: Optional[str] = None

    netmask: Optional[str] = None

    version: Optional[int] = None
    """IP version (`1` for IPv4, `2` for IPv6, `0` if unknown)."""


class ISPIPV4Location(BaseModel):
    city: Optional[str] = None

    country_iso: Optional[str] = None

    state_iso: Optional[str] = None

    zip: Optional[str] = None


class ISPIPV4(BaseModel):
    address: Optional[str] = None

    asn: Optional[int] = None

    aso: Optional[str] = None

    location: Optional[ISPIPV4Location] = None

    name: Optional[str] = None

    netmask: Optional[str] = None

    version: Optional[int] = None
    """IP version (`1` for IPv4, `2` for IPv6, `0` if unknown)."""


class ISPIPV6Location(BaseModel):
    city: Optional[str] = None

    country_iso: Optional[str] = None

    state_iso: Optional[str] = None

    zip: Optional[str] = None


class ISPIPV6(BaseModel):
    address: Optional[str] = None

    asn: Optional[int] = None

    aso: Optional[str] = None

    location: Optional[ISPIPV6Location] = None

    name: Optional[str] = None

    netmask: Optional[str] = None

    version: Optional[int] = None
    """IP version (`1` for IPv4, `2` for IPv6, `0` if unknown)."""


class RamUsedPctByApp(BaseModel):
    name: Optional[str] = None
    """Application name."""

    ram_used_pct: Optional[float] = None
    """RAM usage percentage, on a scale of 0 to 100."""


class RTTMinRTTUs(BaseModel):
    """Minimum round-trip time in microseconds."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class RTTRTTUs(BaseModel):
    """Round-trip time in microseconds."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class RTTRTTVarUs(BaseModel):
    """Round-trip time variance in microseconds."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class RTT(BaseModel):
    """Round-trip time statistics for the WARP tunnel."""

    min_rtt_us: Optional[RTTMinRTTUs] = FieldInfo(alias="minRttUs", default=None)
    """Minimum round-trip time in microseconds."""

    rtt_us: Optional[RTTRTTUs] = FieldInfo(alias="rttUs", default=None)
    """Round-trip time in microseconds."""

    rtt_var_us: Optional[RTTRTTVarUs] = FieldInfo(alias="rttVarUs", default=None)
    """Round-trip time variance in microseconds."""


class TunnelStatsBytesLost(BaseModel):
    """Number of bytes lost, split by direction."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class TunnelStatsBytesReceived(BaseModel):
    """Number of bytes received, split by direction."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class TunnelStatsBytesRetransmitted(BaseModel):
    """Number of bytes retransmitted, split by direction."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class TunnelStatsBytesSent(BaseModel):
    """Number of bytes sent, split by direction."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class TunnelStatsPacketsLost(BaseModel):
    """Number of packets lost, split by direction."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class TunnelStatsPacketsReceived(BaseModel):
    """Number of packets received, split by direction."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class TunnelStatsPacketsRetransmitted(BaseModel):
    """Number of packets retransmitted, split by direction."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class TunnelStatsPacketsSent(BaseModel):
    """Number of packets sent, split by direction."""

    downstream: Optional[int] = None

    upstream: Optional[int] = None


class TunnelStats(BaseModel):
    """WARP tunnel packet and byte counters."""

    bytes_lost: Optional[TunnelStatsBytesLost] = FieldInfo(alias="bytesLost", default=None)
    """Number of bytes lost, split by direction."""

    bytes_received: Optional[TunnelStatsBytesReceived] = FieldInfo(alias="bytesReceived", default=None)
    """Number of bytes received, split by direction."""

    bytes_retransmitted: Optional[TunnelStatsBytesRetransmitted] = FieldInfo(alias="bytesRetransmitted", default=None)
    """Number of bytes retransmitted, split by direction."""

    bytes_sent: Optional[TunnelStatsBytesSent] = FieldInfo(alias="bytesSent", default=None)
    """Number of bytes sent, split by direction."""

    packets_lost: Optional[TunnelStatsPacketsLost] = FieldInfo(alias="packetsLost", default=None)
    """Number of packets lost, split by direction."""

    packets_received: Optional[TunnelStatsPacketsReceived] = FieldInfo(alias="packetsReceived", default=None)
    """Number of packets received, split by direction."""

    packets_retransmitted: Optional[TunnelStatsPacketsRetransmitted] = FieldInfo(
        alias="packetsRetransmitted", default=None
    )
    """Number of packets retransmitted, split by direction."""

    packets_sent: Optional[TunnelStatsPacketsSent] = FieldInfo(alias="packetsSent", default=None)
    """Number of packets sent, split by direction."""

    stats_window_ms: Optional[int] = FieldInfo(alias="statsWindowMs", default=None)
    """The measurement window duration in milliseconds."""


class DeviceListResponse(BaseModel):
    colo: str
    """Cloudflare colo airport code."""

    device_id: str = FieldInfo(alias="deviceId")
    """Device identifier (UUID v4)"""

    mode: str
    """The mode under which the WARP client is run."""

    platform: str
    """Operating system."""

    status: str
    """Network status."""

    timestamp: str

    version: str
    """WARP client version."""

    always_on: Optional[bool] = FieldInfo(alias="alwaysOn", default=None)

    battery_charging: Optional[bool] = FieldInfo(alias="batteryCharging", default=None)

    battery_cycles: Optional[int] = FieldInfo(alias="batteryCycles", default=None)

    battery_pct: Optional[float] = FieldInfo(alias="batteryPct", default=None)

    connection_type: Optional[str] = FieldInfo(alias="connectionType", default=None)

    cpu_pct: Optional[float] = FieldInfo(alias="cpuPct", default=None)

    cpu_pct_by_app: Optional[List[CPUPctByApp]] = FieldInfo(alias="cpuPctByApp", default=None)

    device_ipv4: Optional[DeviceIPV4] = FieldInfo(alias="deviceIpv4", default=None)

    device_ipv6: Optional[DeviceIPV6] = FieldInfo(alias="deviceIpv6", default=None)

    device_name: Optional[str] = FieldInfo(alias="deviceName", default=None)
    """Device identifier (human readable)."""

    device_registration: Optional[str] = FieldInfo(alias="deviceRegistration", default=None)
    """Deprecated: use registrationId. Device registration identifier (UUID)."""

    disk_read_bps: Optional[int] = FieldInfo(alias="diskReadBps", default=None)

    disk_usage_pct: Optional[float] = FieldInfo(alias="diskUsagePct", default=None)

    disk_write_bps: Optional[int] = FieldInfo(alias="diskWriteBps", default=None)

    doh_subdomain: Optional[str] = FieldInfo(alias="dohSubdomain", default=None)

    estimated_loss_pct: Optional[float] = FieldInfo(alias="estimatedLossPct", default=None)

    firewall_enabled: Optional[bool] = FieldInfo(alias="firewallEnabled", default=None)

    gateway_ipv4: Optional[GatewayIPV4] = FieldInfo(alias="gatewayIpv4", default=None)

    gateway_ipv6: Optional[GatewayIPV6] = FieldInfo(alias="gatewayIpv6", default=None)

    handshake_latency_ms: Optional[float] = FieldInfo(alias="handshakeLatencyMs", default=None)

    isp_ipv4: Optional[ISPIPV4] = FieldInfo(alias="ispIpv4", default=None)

    isp_ipv6: Optional[ISPIPV6] = FieldInfo(alias="ispIpv6", default=None)

    metal: Optional[str] = None

    network_rcvd_bps: Optional[int] = FieldInfo(alias="networkRcvdBps", default=None)

    network_sent_bps: Optional[int] = FieldInfo(alias="networkSentBps", default=None)

    network_ssid: Optional[str] = FieldInfo(alias="networkSsid", default=None)

    person_email: Optional[str] = FieldInfo(alias="personEmail", default=None)
    """User contact email address"""

    ram_available_kb: Optional[int] = FieldInfo(alias="ramAvailableKb", default=None)

    ram_used_pct: Optional[float] = FieldInfo(alias="ramUsedPct", default=None)

    ram_used_pct_by_app: Optional[List[RamUsedPctByApp]] = FieldInfo(alias="ramUsedPctByApp", default=None)

    registration_id: Optional[str] = FieldInfo(alias="registrationId", default=None)
    """Device registration identifier (UUID v4).

    On multi-user devices, this uniquely identifies a user's registration on the
    device.
    """

    rtt: Optional[RTT] = None
    """Round-trip time statistics for the WARP tunnel."""

    switch_locked: Optional[bool] = FieldInfo(alias="switchLocked", default=None)

    tunnel_stats: Optional[TunnelStats] = FieldInfo(alias="tunnelStats", default=None)
    """WARP tunnel packet and byte counters."""

    tunnel_type: Optional[str] = FieldInfo(alias="tunnelType", default=None)

    wifi_strength_dbm: Optional[int] = FieldInfo(alias="wifiStrengthDbm", default=None)
