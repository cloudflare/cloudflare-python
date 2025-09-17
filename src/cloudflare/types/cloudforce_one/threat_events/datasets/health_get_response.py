# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "HealthGetResponse",
    "Properties",
    "PropertiesDurationMs",
    "PropertiesOk",
    "PropertiesShards",
    "PropertiesShardsItems",
    "PropertiesShardsItemsProperties",
    "PropertiesShardsItemsPropertiesDatasetID",
    "PropertiesShardsItemsPropertiesDate",
    "PropertiesShardsItemsPropertiesHealthCheckMs",
    "PropertiesShardsItemsPropertiesPageCount",
    "PropertiesShardsItemsPropertiesPageSize",
    "PropertiesShardsItemsPropertiesSizeBytes",
    "PropertiesShardsItemsPropertiesSizeMB",
    "PropertiesShardsItemsPropertiesStartupMs",
    "PropertiesShardsItemsPropertiesTableStats",
    "PropertiesShardsItemsPropertiesTableStatsAdditionalProperties",
    "PropertiesShardsItemsPropertiesTimedOut",
    "PropertiesShardsItemsPropertiesTotalMs",
    "PropertiesTotalShards",
    "PropertiesTotalSizeBytes",
    "PropertiesTotalSizeMB",
]


class PropertiesDurationMs(BaseModel):
    type: str


class PropertiesOk(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesDatasetID(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesDate(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesHealthCheckMs(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesPageCount(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesPageSize(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesSizeBytes(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesSizeMB(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesStartupMs(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesTableStatsAdditionalProperties(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesTableStats(BaseModel):
    additional_properties: PropertiesShardsItemsPropertiesTableStatsAdditionalProperties = FieldInfo(
        alias="additionalProperties"
    )

    type: str


class PropertiesShardsItemsPropertiesTimedOut(BaseModel):
    type: str


class PropertiesShardsItemsPropertiesTotalMs(BaseModel):
    type: str


class PropertiesShardsItemsProperties(BaseModel):
    dataset_id: PropertiesShardsItemsPropertiesDatasetID = FieldInfo(alias="datasetId")

    date: PropertiesShardsItemsPropertiesDate

    health_check_ms: PropertiesShardsItemsPropertiesHealthCheckMs = FieldInfo(alias="healthCheckMs")

    page_count: PropertiesShardsItemsPropertiesPageCount = FieldInfo(alias="pageCount")

    page_size: PropertiesShardsItemsPropertiesPageSize = FieldInfo(alias="pageSize")

    size_bytes: PropertiesShardsItemsPropertiesSizeBytes = FieldInfo(alias="sizeBytes")

    size_mb: PropertiesShardsItemsPropertiesSizeMB = FieldInfo(alias="sizeMB")

    startup_ms: PropertiesShardsItemsPropertiesStartupMs = FieldInfo(alias="startupMs")

    table_stats: PropertiesShardsItemsPropertiesTableStats = FieldInfo(alias="tableStats")

    timed_out: PropertiesShardsItemsPropertiesTimedOut = FieldInfo(alias="timedOut")

    total_ms: PropertiesShardsItemsPropertiesTotalMs = FieldInfo(alias="totalMs")


class PropertiesShardsItems(BaseModel):
    properties: PropertiesShardsItemsProperties

    type: str


class PropertiesShards(BaseModel):
    items: PropertiesShardsItems

    type: str


class PropertiesTotalShards(BaseModel):
    type: str


class PropertiesTotalSizeBytes(BaseModel):
    type: str


class PropertiesTotalSizeMB(BaseModel):
    type: str


class Properties(BaseModel):
    duration_ms: PropertiesDurationMs = FieldInfo(alias="durationMs")

    ok: PropertiesOk

    shards: PropertiesShards

    total_shards: PropertiesTotalShards = FieldInfo(alias="totalShards")

    total_size_bytes: PropertiesTotalSizeBytes = FieldInfo(alias="totalSizeBytes")

    total_size_mb: PropertiesTotalSizeMB = FieldInfo(alias="totalSizeMB")


class HealthGetResponse(BaseModel):
    properties: Properties

    type: str
