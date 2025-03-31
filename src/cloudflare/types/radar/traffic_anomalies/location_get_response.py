# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LocationGetResponse"]


class LocationGetResponse(BaseModel):
    traffic_anomalies: List[object] = FieldInfo(alias="trafficAnomalies")
