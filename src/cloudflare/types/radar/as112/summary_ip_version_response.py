# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...unnamed_schema_ref_128 import UnnamedSchemaRef128
from ...unnamed_schema_ref_174 import UnnamedSchemaRef174
from ...unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["SummaryIPVersionResponse", "Meta", "MetaConfidenceInfo"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRef174]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class SummaryIPVersionResponse(BaseModel):
    meta: Meta

    summary_0: UnnamedSchemaRef128
