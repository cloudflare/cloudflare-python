# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...unnamed_schema_ref_b5f3bd1840490bc487ffef84567807b1 import UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1
from ...unnamed_schema_ref_baac9d7da12de53e99142f8ecd3982e5 import UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5

__all__ = ["TopBotsResponse", "Meta", "MetaConfidenceInfo", "Top0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5] = FieldInfo(alias="dateRange")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Top0(BaseModel):
    bot_category: str = FieldInfo(alias="botCategory")

    bot_name: str = FieldInfo(alias="botName")

    bot_owner: str = FieldInfo(alias="botOwner")

    value: str


class TopBotsResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
