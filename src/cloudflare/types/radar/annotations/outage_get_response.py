# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "OutageGetResponse",
    "Annotation",
    "AnnotationASNsDetail",
    "AnnotationASNsDetailLocation",
    "AnnotationEntity",
    "AnnotationLocationsDetail",
    "AnnotationOriginsDetail",
    "AnnotationOutage",
]


class AnnotationASNsDetailLocation(BaseModel):
    code: str

    name: str


class AnnotationASNsDetail(BaseModel):
    asn: str

    location: Optional[AnnotationASNsDetailLocation] = None

    name: Optional[str] = None


class AnnotationEntity(BaseModel):
    entity_name: Optional[str] = FieldInfo(alias="entityName", default=None)

    entity_type: str = FieldInfo(alias="entityType")

    entity_value: str = FieldInfo(alias="entityValue")


class AnnotationLocationsDetail(BaseModel):
    code: str

    name: str


class AnnotationOriginsDetail(BaseModel):
    name: Optional[str] = None

    origin: str


class AnnotationOutage(BaseModel):
    outage_cause: str = FieldInfo(alias="outageCause")

    outage_type: str = FieldInfo(alias="outageType")


class Annotation(BaseModel):
    id: str

    asns: List[int]

    asns_details: List[AnnotationASNsDetail] = FieldInfo(alias="asnsDetails")

    data_source: str = FieldInfo(alias="dataSource")

    description: Optional[str] = None

    end_date: Optional[datetime] = FieldInfo(alias="endDate", default=None)

    entities: List[AnnotationEntity]

    event_type: str = FieldInfo(alias="eventType")

    geo_ids: List[str] = FieldInfo(alias="geoIds")

    linked_url: Optional[str] = FieldInfo(alias="linkedUrl", default=None)

    locations: List[str]

    locations_details: List[Optional[AnnotationLocationsDetail]] = FieldInfo(alias="locationsDetails")

    origins: List[str]

    origins_details: List[AnnotationOriginsDetail] = FieldInfo(alias="originsDetails")

    outage: Optional[AnnotationOutage] = None

    scope: Optional[str] = None

    start_date: datetime = FieldInfo(alias="startDate")

    tags: List[str]


class OutageGetResponse(BaseModel):
    annotations: List[Annotation]
