# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TCPResetsTimeoutTimeseriesGroupsResponse", "Meta", "MetaConfidenceInfo", "Serie0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[object]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    agg_interval: str = FieldInfo(alias="aggInterval")

    date_range: List[object] = FieldInfo(alias="dateRange")

    last_updated: datetime = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Serie0(BaseModel):
    later_in_flow: List[str]

    no_match: List[str]

    post_ack: List[str]

    post_psh: List[str]

    post_syn: List[str]

    timestamps: List[datetime]


class TCPResetsTimeoutTimeseriesGroupsResponse(BaseModel):
    meta: Meta

    serie_0: Serie0
