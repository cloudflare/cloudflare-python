# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TopBotsResponse", "Meta", "MetaConfidenceInfo", "Top0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Top0(BaseModel):
    bot_category: str = FieldInfo(alias="botCategory")

    bot_name: str = FieldInfo(alias="botName")

    bot_owner: str = FieldInfo(alias="botOwner")

    value: str


class TopBotsResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
