# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from datetime import datetime

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AseGetResponse", "Meta", "MetaDateRange", "Top0"]


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")


class Top0(BaseModel):
    asn: int

    as_name: str = FieldInfo(alias="ASName")

    value: str
    """
    Percentage of updates by this AS out of the total updates by all autonomous
    systems.
    """


class AseGetResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
