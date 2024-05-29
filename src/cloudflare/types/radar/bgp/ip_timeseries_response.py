# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IPTimeseriesResponse", "Meta", "MetaDateRange", "Serie174", "SerieCn"]


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")


class Serie174(BaseModel):
    ipv4: List[str]

    ipv6: List[str]

    timestamps: List[datetime]


class SerieCn(BaseModel):
    ipv4: List[str]

    ipv6: List[str]

    timestamps: List[datetime]


class IPTimeseriesResponse(BaseModel):
    meta: Meta

    serie_174: Serie174

    serie_cn: SerieCn
