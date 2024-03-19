# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "DigitalExperienceMonitoringTracerouteTestNetworkPath",
    "NetworkPath",
    "NetworkPathSlot",
    "NetworkPathSampling",
]


class NetworkPathSlot(BaseModel):
    id: str
    """API Resource UUID tag."""

    client_to_app_rtt_ms: Optional[int] = FieldInfo(alias="clientToAppRttMs", default=None)
    """Round trip time in ms of the client to app mile"""

    client_to_cf_egress_rtt_ms: Optional[int] = FieldInfo(alias="clientToCfEgressRttMs", default=None)
    """Round trip time in ms of the client to Cloudflare egress mile"""

    client_to_cf_ingress_rtt_ms: Optional[int] = FieldInfo(alias="clientToCfIngressRttMs", default=None)
    """Round trip time in ms of the client to Cloudflare ingress mile"""

    timestamp: str

    client_to_isp_rtt_ms: Optional[int] = FieldInfo(alias="clientToIspRttMs", default=None)
    """Round trip time in ms of the client to ISP mile"""


class NetworkPathSampling(BaseModel):
    unit: Literal["hours"]

    value: int


class NetworkPath(BaseModel):
    slots: List[NetworkPathSlot]

    sampling: Optional[NetworkPathSampling] = None
    """Specifies the sampling applied, if any, to the slots response.

    When sampled, results shown represent the first test run to the start of each
    sampling interval.
    """


class DigitalExperienceMonitoringTracerouteTestNetworkPath(BaseModel):
    id: str
    """API Resource UUID tag."""

    device_name: Optional[str] = FieldInfo(alias="deviceName", default=None)

    interval: Optional[str] = None
    """The interval at which the Traceroute synthetic application test is set to run."""

    kind: Optional[Literal["traceroute"]] = None

    name: Optional[str] = None

    network_path: Optional[NetworkPath] = FieldInfo(alias="networkPath", default=None)

    url: Optional[str] = None
    """The host of the Traceroute synthetic application test"""
