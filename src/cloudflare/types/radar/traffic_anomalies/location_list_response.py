# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["LocationListResponse", "TrafficAnomaly"]


class TrafficAnomaly(BaseModel):
    client_country_alpha2: str = FieldInfo(alias="clientCountryAlpha2")

    client_country_name: str = FieldInfo(alias="clientCountryName")

    value: str


class LocationListResponse(BaseModel):
    traffic_anomalies: List[TrafficAnomaly] = FieldInfo(alias="trafficAnomalies")
