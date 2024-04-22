# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..unnamed_schema_ref_106 import UnnamedSchemaRef106

__all__ = ["TrafficAnomalyGetResponse", "TrafficAnomaly", "TrafficAnomalyASNDetails"]


class TrafficAnomalyASNDetails(BaseModel):
    asn: str

    name: str

    locations: Optional[UnnamedSchemaRef106] = None


class TrafficAnomaly(BaseModel):
    start_date: str = FieldInfo(alias="startDate")

    status: str

    type: str

    uuid: str

    asn_details: Optional[TrafficAnomalyASNDetails] = FieldInfo(alias="asnDetails", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    location_details: Optional[UnnamedSchemaRef106] = FieldInfo(alias="locationDetails", default=None)

    visible_in_data_sources: Optional[List[str]] = FieldInfo(alias="visibleInDataSources", default=None)


class TrafficAnomalyGetResponse(BaseModel):
    traffic_anomalies: List[TrafficAnomaly] = FieldInfo(alias="trafficAnomalies")
