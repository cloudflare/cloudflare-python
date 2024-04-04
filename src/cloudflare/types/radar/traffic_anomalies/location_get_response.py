# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...unnamed_schema_ref_160 import UnnamedSchemaRef160

__all__ = ["LocationGetResponse"]


class LocationGetResponse(BaseModel):
    traffic_anomalies: List[UnnamedSchemaRef160] = FieldInfo(alias="trafficAnomalies")
