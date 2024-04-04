# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...unnamed_schema_ref_83a14d589e799bc901b9ccc870251d09 import UnnamedSchemaRef83a14d589e799bc901b9ccc870251d09

__all__ = ["LocationGetResponse"]


class LocationGetResponse(BaseModel):
    traffic_anomalies: List[UnnamedSchemaRef83a14d589e799bc901b9ccc870251d09] = FieldInfo(alias="trafficAnomalies")
