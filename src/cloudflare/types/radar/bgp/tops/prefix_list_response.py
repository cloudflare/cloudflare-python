# File generated from our OpenAPI spec by Stainless.

from datetime import datetime

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = ["PrefixListResponse", "Meta", "MetaDateRange", "Top0"]


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")


class Top0(BaseModel):
    prefix: str

    value: str


class PrefixListResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
