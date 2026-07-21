# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["IndicatorListResponse", "Indicator", "IndicatorRelatedEvent", "IndicatorTag", "Pagination"]


class IndicatorRelatedEvent(BaseModel):
    dataset_id: str = FieldInfo(alias="datasetId")

    event_id: str = FieldInfo(alias="eventId")


class IndicatorTag(BaseModel):
    category_name: Optional[str] = FieldInfo(alias="categoryName", default=None)

    uuid: Optional[str] = None

    value: Optional[str] = None


class Indicator(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    indicator_type: str = FieldInfo(alias="indicatorType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    uuid: str

    value: str

    dataset_id: Optional[str] = FieldInfo(alias="datasetId", default=None)
    """The dataset ID this indicator belongs to. Included in list responses."""

    related_events: Optional[List[IndicatorRelatedEvent]] = FieldInfo(alias="relatedEvents", default=None)

    tags: Optional[List[IndicatorTag]] = None


class Pagination(BaseModel):
    page: float

    page_size: float = FieldInfo(alias="pageSize")

    total_count: float = FieldInfo(alias="totalCount")

    total_pages: float = FieldInfo(alias="totalPages")


class IndicatorListResponse(BaseModel):
    indicators: List[Indicator]

    pagination: Pagination
