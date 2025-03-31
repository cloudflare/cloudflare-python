# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["UserAgentDirectiveResponse", "Meta", "MetaConfidenceInfo", "MetaUnit", "Top0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class MetaUnit(BaseModel):
    name: str

    value: str


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)

    units: Optional[List[MetaUnit]] = None


class Top0(BaseModel):
    name: str

    value: int

    fully: Optional[int] = None

    partially: Optional[int] = None


class UserAgentDirectiveResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
