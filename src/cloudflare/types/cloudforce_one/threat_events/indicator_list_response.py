# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "IndicatorListResponse",
    "Properties",
    "PropertiesCompleteness",
    "PropertiesCompletenessProperties",
    "PropertiesCompletenessPropertiesComplete",
    "PropertiesCompletenessPropertiesFailedDatasets",
    "PropertiesCompletenessPropertiesFailedDatasetsItems",
    "PropertiesCompletenessPropertiesFailedShards",
    "PropertiesCompletenessPropertiesFailedShardsItems",
    "PropertiesCompletenessPropertiesFailedShardsItemsProperties",
    "PropertiesCompletenessPropertiesFailedShardsItemsPropertiesDatasetID",
    "PropertiesCompletenessPropertiesFailedShardsItemsPropertiesShardID",
    "PropertiesCompletenessPropertiesWarnings",
    "PropertiesCompletenessPropertiesWarningsItems",
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
    "PropertiesPaginationPropertiesTotalCountIsExact",
]


class PropertiesCompletenessPropertiesComplete(BaseModel):
    type: str


class PropertiesCompletenessPropertiesFailedDatasetsItems(BaseModel):
    type: str


class PropertiesCompletenessPropertiesFailedDatasets(BaseModel):
    items: PropertiesCompletenessPropertiesFailedDatasetsItems

    type: str


class PropertiesCompletenessPropertiesFailedShardsItemsPropertiesDatasetID(BaseModel):
    type: str


class PropertiesCompletenessPropertiesFailedShardsItemsPropertiesShardID(BaseModel):
    type: str


class PropertiesCompletenessPropertiesFailedShardsItemsProperties(BaseModel):
    dataset_id: PropertiesCompletenessPropertiesFailedShardsItemsPropertiesDatasetID = FieldInfo(alias="datasetId")

    shard_id: PropertiesCompletenessPropertiesFailedShardsItemsPropertiesShardID = FieldInfo(alias="shardId")


class PropertiesCompletenessPropertiesFailedShardsItems(BaseModel):
    properties: PropertiesCompletenessPropertiesFailedShardsItemsProperties

    type: str


class PropertiesCompletenessPropertiesFailedShards(BaseModel):
    items: PropertiesCompletenessPropertiesFailedShardsItems

    type: str


class PropertiesCompletenessPropertiesWarningsItems(BaseModel):
    type: str


class PropertiesCompletenessPropertiesWarnings(BaseModel):
    items: PropertiesCompletenessPropertiesWarningsItems

    type: str


class PropertiesCompletenessProperties(BaseModel):
    complete: PropertiesCompletenessPropertiesComplete

    failed_datasets: PropertiesCompletenessPropertiesFailedDatasets = FieldInfo(alias="failedDatasets")

    failed_shards: PropertiesCompletenessPropertiesFailedShards = FieldInfo(alias="failedShards")

    warnings: PropertiesCompletenessPropertiesWarnings


class PropertiesCompleteness(BaseModel):
    properties: PropertiesCompletenessProperties

    type: str


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
    description: str

    nullable: bool

    type: str


class PropertiesPaginationPropertiesTotalCountIsExact(BaseModel):
    description: str

    type: str


class PropertiesPaginationProperties(BaseModel):
    count: PropertiesPaginationPropertiesCount

    page: PropertiesPaginationPropertiesPage

    per_page: PropertiesPaginationPropertiesPerPage

    total_count: PropertiesPaginationPropertiesTotalCount

    total_count_is_exact: PropertiesPaginationPropertiesTotalCountIsExact


class PropertiesPagination(BaseModel):
    properties: PropertiesPaginationProperties

    type: str


class Properties(BaseModel):
    completeness: PropertiesCompleteness

    indicators: PropertiesIndicators

    pagination: PropertiesPagination


class IndicatorListResponse(BaseModel):
    properties: Properties

    type: str
