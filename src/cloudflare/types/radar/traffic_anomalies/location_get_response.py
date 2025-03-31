# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LocationGetResponse", "TrafficAnomaly"]


class TrafficAnomaly(BaseModel):
    client_country_alpha2: str = FieldInfo(alias="clientCountryAlpha2")

    client_country_name: str = FieldInfo(alias="clientCountryName")

    value: str


class LocationGetResponse(BaseModel):
    traffic_anomalies: List[TrafficAnomaly] = FieldInfo(alias="trafficAnomalies")
