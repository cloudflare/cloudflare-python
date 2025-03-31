# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ......_models import BaseModel

__all__ = ["LocationTargetResponse", "Meta", "MetaConfidenceInfo", "Top0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Top0(BaseModel):
    rank: float

    target_country_alpha2: str = FieldInfo(alias="targetCountryAlpha2")

    target_country_name: str = FieldInfo(alias="targetCountryName")

    value: str


class LocationTargetResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
