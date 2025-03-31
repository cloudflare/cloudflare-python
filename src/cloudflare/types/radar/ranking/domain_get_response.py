# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DomainGetResponse", "Details0", "Details0Category", "Details0TopLocation", "Meta"]


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


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")


class DomainGetResponse(BaseModel):
    details_0: Details0

    meta: Meta
