# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DomainGetResponse", "Details0", "Details0Category", "Details0TopLocation", "Meta", "MetaDateRange"]


class Details0Category(BaseModel):
    id: int

    name: str

    super_category_id: int = FieldInfo(alias="superCategoryId")


class Details0TopLocation(BaseModel):
    location_code: str = FieldInfo(alias="locationCode")

    location_name: str = FieldInfo(alias="locationName")

    rank: int


class Details0(BaseModel):
    categories: List[Details0Category]

    bucket: Optional[str] = None
    """Only available in POPULAR ranking for the most recent ranking."""

    rank: Optional[int] = None

    top_locations: Optional[List[Details0TopLocation]] = None


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")


class DomainGetResponse(BaseModel):
    details_0: Details0

    meta: Meta
