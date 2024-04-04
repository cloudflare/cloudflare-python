# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["RouteTimeseriesResponse", "Meta", "SerieIPV4_24s", "SerieIPV6_48s"]


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")


class SerieIPV4_24s(BaseModel):
    timestamps: List[datetime]

    values: List[int]


class SerieIPV6_48s(BaseModel):
    timestamps: List[datetime]

    values: List[int]


class RouteTimeseriesResponse(BaseModel):
    meta: Meta

    serie_ipv4_24s: SerieIPV4_24s

    serie_ipv6_48s: SerieIPV6_48s
