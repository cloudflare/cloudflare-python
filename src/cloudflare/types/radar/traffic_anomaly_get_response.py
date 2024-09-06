# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = [
    "TrafficAnomalyGetResponse",
    "TrafficAnomaly",
    "TrafficAnomalyASNDetails",
    "TrafficAnomalyASNDetailsLocations",
    "TrafficAnomalyLocationDetails",
]


class TrafficAnomalyASNDetailsLocations(BaseModel):
    code: str

    name: str


class TrafficAnomalyASNDetails(BaseModel):
    asn: str

    name: str

    locations: Optional[TrafficAnomalyASNDetailsLocations] = None


class TrafficAnomalyLocationDetails(BaseModel):
    code: str

    name: str


class TrafficAnomaly(BaseModel):
    start_date: str = FieldInfo(alias="startDate")

    status: str

    type: str

    uuid: str

    asn_details: Optional[TrafficAnomalyASNDetails] = FieldInfo(alias="asnDetails", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    location_details: Optional[TrafficAnomalyLocationDetails] = FieldInfo(alias="locationDetails", default=None)

    visible_in_data_sources: Optional[List[str]] = FieldInfo(alias="visibleInDataSources", default=None)


class TrafficAnomalyGetResponse(BaseModel):
    traffic_anomalies: List[TrafficAnomaly] = FieldInfo(alias="trafficAnomalies")
