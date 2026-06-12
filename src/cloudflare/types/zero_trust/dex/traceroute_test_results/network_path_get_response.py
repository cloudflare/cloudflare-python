# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["NetworkPathGetResponse", "Hop", "HopLocation"]


class HopLocation(BaseModel):
    city: Optional[str] = None

    state: Optional[str] = None

    zip: Optional[str] = None


class Hop(BaseModel):
    ttl: int

    asn: Optional[int] = None

    aso: Optional[str] = None

    ip_address: Optional[str] = FieldInfo(alias="ipAddress", default=None)

    location: Optional[HopLocation] = None

    mile: Optional[Literal["client-to-app", "client-to-cf-egress", "client-to-cf-ingress", "client-to-isp"]] = None

    name: Optional[str] = None

    packet_loss_pct: Optional[float] = FieldInfo(alias="packetLossPct", default=None)

    rtt_ms: Optional[int] = FieldInfo(alias="rttMs", default=None)


class NetworkPathGetResponse(BaseModel):
    hops: List[Hop]
    """An array of the hops taken by the device to reach the end destination."""

    result_id: str = FieldInfo(alias="resultId")
    """API Resource UUID tag."""

    colo: Optional[str] = None
    """Cloudflare colo airport code."""

    device_name: Optional[str] = FieldInfo(alias="deviceName", default=None)
    """Name of the device associated with this network path response."""

    execution_context: Optional[Literal["EXECUTION_CONTEXT_INVALID", "OUT_OF_TUNNEL", "IN_TUNNEL"]] = None
    """Whether the test was run inside or outside of the WARP tunnel."""

    test_id: Optional[str] = FieldInfo(alias="testId", default=None)
    """API Resource UUID tag."""

    test_name: Optional[str] = FieldInfo(alias="testName", default=None)
    """Name of the traceroute test."""

    time_start: Optional[str] = None
    """Timestamp indicating when the traceroute test execution began."""

    tunnel_type: Optional[str] = None
