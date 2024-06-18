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
    """an array of the hops taken by the device to reach the end destination"""

    result_id: str = FieldInfo(alias="resultId")
    """API Resource UUID tag."""

    device_name: Optional[str] = FieldInfo(alias="deviceName", default=None)
    """name of the device associated with this network path response"""

    test_id: Optional[str] = FieldInfo(alias="testId", default=None)
    """API Resource UUID tag."""

    test_name: Optional[str] = FieldInfo(alias="testName", default=None)
    """name of the tracroute test"""
