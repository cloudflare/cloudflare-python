# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "IndicatorListResponse",
    "Properties",
    "PropertiesIndicators",
    "PropertiesIndicatorsItems",
    "PropertiesIndicatorsItemsRelatedEvent",
    "PropertiesIndicatorsItemsTag",
    "PropertiesPagination",
    "PropertiesPaginationProperties",
    "PropertiesPaginationPropertiesCount",
    "PropertiesPaginationPropertiesPage",
    "PropertiesPaginationPropertiesPerPage",
    "PropertiesPaginationPropertiesTotalCount",
]


class PropertiesIndicatorsItemsRelatedEvent(BaseModel):
    dataset_id: str = FieldInfo(alias="datasetId")

    event_id: str = FieldInfo(alias="eventId")


class PropertiesIndicatorsItemsTag(BaseModel):
    category_name: Optional[str] = FieldInfo(alias="categoryName", default=None)

    uuid: Optional[str] = None

    value: Optional[str] = None


class PropertiesIndicatorsItems(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    indicator_type: str = FieldInfo(alias="indicatorType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    uuid: str

    value: str

    dataset_id: Optional[str] = FieldInfo(alias="datasetId", default=None)
    """The dataset ID this indicator belongs to. Included in list responses."""

    related_events: Optional[List[PropertiesIndicatorsItemsRelatedEvent]] = FieldInfo(
        alias="relatedEvents", default=None
    )

    tags: Optional[List[PropertiesIndicatorsItemsTag]] = None


class PropertiesIndicators(BaseModel):
    items: PropertiesIndicatorsItems

    type: str


class PropertiesPaginationPropertiesCount(BaseModel):
    type: str


class PropertiesPaginationPropertiesPage(BaseModel):
    type: str


class PropertiesPaginationPropertiesPerPage(BaseModel):
    type: str


class PropertiesPaginationPropertiesTotalCount(BaseModel):
    type: str


class PropertiesPaginationProperties(BaseModel):
    count: PropertiesPaginationPropertiesCount

    page: PropertiesPaginationPropertiesPage

    per_page: PropertiesPaginationPropertiesPerPage

    total_count: PropertiesPaginationPropertiesTotalCount


class PropertiesPagination(BaseModel):
    properties: PropertiesPaginationProperties

    type: str


class Properties(BaseModel):
    indicators: PropertiesIndicators

    pagination: PropertiesPagination


class IndicatorListResponse(BaseModel):
    properties: Properties

    type: str
