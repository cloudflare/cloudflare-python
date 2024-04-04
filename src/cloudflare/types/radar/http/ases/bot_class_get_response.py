# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ....unnamed_schema_ref_174 import UnnamedSchemaRef174
from ....unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["BotClassGetResponse", "Meta", "MetaConfidenceInfo", "Top0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRef174]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Top0(BaseModel):
    client_asn: int = FieldInfo(alias="clientASN")

    client_as_name: str = FieldInfo(alias="clientASName")

    value: str


class BotClassGetResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
