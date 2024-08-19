# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "OutageGetResponse",
    "Annotation",
    "AnnotationASNsDetail",
    "AnnotationASNsDetailLocations",
    "AnnotationLocationsDetail",
    "AnnotationOutage",
]


class AnnotationASNsDetailLocations(BaseModel):
    code: str

    name: str


class AnnotationASNsDetail(BaseModel):
    asn: str

    name: str

    locations: Optional[AnnotationASNsDetailLocations] = None


class AnnotationLocationsDetail(BaseModel):
    code: str

    name: str


class AnnotationOutage(BaseModel):
    outage_cause: str = FieldInfo(alias="outageCause")

    outage_type: str = FieldInfo(alias="outageType")


class Annotation(BaseModel):
    id: str

    asns: List[int]

    asns_details: List[AnnotationASNsDetail] = FieldInfo(alias="asnsDetails")

    data_source: str = FieldInfo(alias="dataSource")

    event_type: str = FieldInfo(alias="eventType")

    locations: List[str]

    locations_details: List[AnnotationLocationsDetail] = FieldInfo(alias="locationsDetails")

    outage: AnnotationOutage

    start_date: str = FieldInfo(alias="startDate")

    description: Optional[str] = None

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    linked_url: Optional[str] = FieldInfo(alias="linkedUrl", default=None)

    scope: Optional[str] = None


class OutageGetResponse(BaseModel):
    annotations: List[Annotation]
