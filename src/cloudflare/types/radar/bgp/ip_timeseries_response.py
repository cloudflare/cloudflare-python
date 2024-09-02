# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IPTimeseriesResponse", "Meta", "MetaQuery", "MetaQueryDateRange", "Serie174"]


class MetaQueryDateRange(BaseModel):
    end_time: str = FieldInfo(alias="endTime")

    start_time: str = FieldInfo(alias="startTime")


class MetaQuery(BaseModel):
    date_range: MetaQueryDateRange = FieldInfo(alias="dateRange")

    entity: str


class Meta(BaseModel):
    queries: List[MetaQuery]


class Serie174(BaseModel):
    ipv4: List[str]

    ipv6: List[str]

    timestamps: List[datetime]


class IPTimeseriesResponse(BaseModel):
    meta: Meta

    serie_174: Serie174
