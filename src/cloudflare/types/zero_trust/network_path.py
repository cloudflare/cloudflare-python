# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NetworkPath", "Slot", "Sampling"]


class Slot(BaseModel):
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


class Sampling(BaseModel):
    unit: Literal["hours"]

    value: int


class NetworkPath(BaseModel):
    slots: List[Slot]

    sampling: Optional[Sampling] = None
    """Specifies the sampling applied, if any, to the slots response.

    When sampled, results shown represent the first test run to the start of each
    sampling interval.
    """
