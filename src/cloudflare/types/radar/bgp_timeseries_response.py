# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..unnamed_schema_ref_129 import UnnamedSchemaRef129
from ..unnamed_schema_ref_174 import UnnamedSchemaRef174
from ..unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["BGPTimeseriesResponse", "Meta", "MetaConfidenceInfo"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRef174]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    agg_interval: str = FieldInfo(alias="aggInterval")

    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")

    last_updated: datetime = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class BGPTimeseriesResponse(BaseModel):
    meta: Meta

    serie_0: UnnamedSchemaRef129
