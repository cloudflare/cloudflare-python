# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["SummaryHTTPVersionResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    http_1_x: str = FieldInfo(alias="HTTP/1.x")

    http_2: str = FieldInfo(alias="HTTP/2")

    http_3: str = FieldInfo(alias="HTTP/3")


class SummaryHTTPVersionResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
