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
]


class CPUPctByApp(BaseModel):
    cpu_pct: Optional[float] = None

    name: Optional[str] = None


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

    netmask: Optional[str] = None

    version: Optional[str] = None


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

    netmask: Optional[str] = None

    version: Optional[str] = None


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

    netmask: Optional[str] = None

    version: Optional[str] = None


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

    netmask: Optional[str] = None

    version: Optional[str] = None


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

    netmask: Optional[str] = None

    version: Optional[str] = None


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

    netmask: Optional[str] = None

    version: Optional[str] = None


class RamUsedPctByApp(BaseModel):
    name: Optional[str] = None

    ram_used_pct: Optional[float] = None


class DeviceListResponse(BaseModel):
    colo: str
    """Cloudflare colo"""

    device_id: str = FieldInfo(alias="deviceId")
    """Device identifier (UUID v4)"""

    mode: str
    """The mode under which the WARP client is run"""

    platform: str
    """Operating system"""

    status: str
    """Network status"""

    timestamp: str
    """Timestamp in ISO format"""

    version: str
    """WARP client version"""

    always_on: Optional[bool] = FieldInfo(alias="alwaysOn", default=None)

    battery_charging: Optional[bool] = FieldInfo(alias="batteryCharging", default=None)

    battery_cycles: Optional[int] = FieldInfo(alias="batteryCycles", default=None)

    battery_pct: Optional[float] = FieldInfo(alias="batteryPct", default=None)

    connection_type: Optional[str] = FieldInfo(alias="connectionType", default=None)

    cpu_pct: Optional[float] = FieldInfo(alias="cpuPct", default=None)

    cpu_pct_by_app: Optional[List[List[CPUPctByApp]]] = FieldInfo(alias="cpuPctByApp", default=None)

    device_ipv4: Optional[DeviceIPV4] = FieldInfo(alias="deviceIpv4", default=None)

    device_ipv6: Optional[DeviceIPV6] = FieldInfo(alias="deviceIpv6", default=None)

    device_name: Optional[str] = FieldInfo(alias="deviceName", default=None)
    """Device identifier (human readable)"""

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

    ram_used_pct_by_app: Optional[List[List[RamUsedPctByApp]]] = FieldInfo(alias="ramUsedPctByApp", default=None)

    switch_locked: Optional[bool] = FieldInfo(alias="switchLocked", default=None)

    wifi_strength_dbm: Optional[int] = FieldInfo(alias="wifiStrengthDbm", default=None)
