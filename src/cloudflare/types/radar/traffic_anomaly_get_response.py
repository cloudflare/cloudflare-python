# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TrafficAnomalyGetResponse",
    "TrafficAnomaly",
    "TrafficAnomalyASNDetails",
    "TrafficAnomalyASNDetailsLocation",
    "TrafficAnomalyLocationDetails",
    "TrafficAnomalyOriginDetails",
]


class TrafficAnomalyASNDetailsLocation(BaseModel):
    code: str

    name: str


class TrafficAnomalyASNDetails(BaseModel):
    asn: str

    location: Optional[TrafficAnomalyASNDetailsLocation] = None

    name: Optional[str] = None


class TrafficAnomalyLocationDetails(BaseModel):
    code: str

    name: str


class TrafficAnomalyOriginDetails(BaseModel):
    name: Optional[str] = None

    origin: str


class TrafficAnomaly(BaseModel):
    asn_details: Optional[TrafficAnomalyASNDetails] = FieldInfo(alias="asnDetails", default=None)

    end_date: Optional[datetime] = FieldInfo(alias="endDate", default=None)

    location_details: Optional[TrafficAnomalyLocationDetails] = FieldInfo(alias="locationDetails", default=None)

    origin_details: Optional[TrafficAnomalyOriginDetails] = FieldInfo(alias="originDetails", default=None)

    start_date: str = FieldInfo(alias="startDate")

    status: str

    type: str

    uuid: str

    visible_in_data_sources: Optional[List[str]] = FieldInfo(alias="visibleInDataSources", default=None)


class TrafficAnomalyGetResponse(BaseModel):
    traffic_anomalies: List[TrafficAnomaly] = FieldInfo(alias="trafficAnomalies")
