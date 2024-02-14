# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "TrafficAnomalyListResponse",
    "TrafficAnomaly",
    "TrafficAnomalyAsnDetails",
    "TrafficAnomalyAsnDetailsLocations",
    "TrafficAnomalyLocationDetails",
]


class TrafficAnomalyAsnDetailsLocations(BaseModel):
    code: str

    name: str


class TrafficAnomalyAsnDetails(BaseModel):
    asn: str

    name: str

    locations: Optional[TrafficAnomalyAsnDetailsLocations] = None


class TrafficAnomalyLocationDetails(BaseModel):
    code: str

    name: str


class TrafficAnomaly(BaseModel):
    start_date: str = FieldInfo(alias="startDate")

    status: str

    type: str

    uuid: str

    asn_details: Optional[TrafficAnomalyAsnDetails] = FieldInfo(alias="asnDetails", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    location_details: Optional[TrafficAnomalyLocationDetails] = FieldInfo(alias="locationDetails", default=None)

    visible_in_data_sources: Optional[List[str]] = FieldInfo(alias="visibleInDataSources", default=None)


class TrafficAnomalyListResponse(BaseModel):
    traffic_anomalies: List[TrafficAnomaly] = FieldInfo(alias="trafficAnomalies")
