# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ....unnamed_schema_ref_174 import UnnamedSchemaRef174
from ....unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["TopAttacksResponse", "Meta", "MetaConfidenceInfo", "Top0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRef174]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Top0(BaseModel):
    origin_country_alpha2: str = FieldInfo(alias="originCountryAlpha2")

    origin_country_name: str = FieldInfo(alias="originCountryName")

    target_country_alpha2: str = FieldInfo(alias="targetCountryAlpha2")

    target_country_name: str = FieldInfo(alias="targetCountryName")

    value: str


class TopAttacksResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
