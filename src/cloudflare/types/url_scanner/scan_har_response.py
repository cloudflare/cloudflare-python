# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ScanHARResponse",
    "HAR",
    "HARLog",
    "HARLogCreator",
    "HARLogEntry",
    "HARLogEntryRequest",
    "HARLogEntryRequestHeader",
    "HARLogEntryResponse",
    "HARLogEntryResponseContent",
    "HARLogEntryResponseHeader",
    "HARLogPage",
    "HARLogPagePageTimings",
]


class HARLogCreator(BaseModel):
    comment: str

    name: str

    version: str


class HARLogEntryRequestHeader(BaseModel):
    name: str

    value: str


class HARLogEntryRequest(BaseModel):
    body_size: float = FieldInfo(alias="bodySize")

    headers: List[HARLogEntryRequestHeader]

    headers_size: float = FieldInfo(alias="headersSize")

    http_version: str = FieldInfo(alias="httpVersion")

    method: str

    url: str


class HARLogEntryResponseContent(BaseModel):
    mime_type: str = FieldInfo(alias="mimeType")

    size: float

    compression: Optional[int] = None


class HARLogEntryResponseHeader(BaseModel):
    name: str

    value: str


class HARLogEntryResponse(BaseModel):
    transfer_size: float = FieldInfo(alias="_transferSize")

    body_size: float = FieldInfo(alias="bodySize")

    content: HARLogEntryResponseContent

    headers: List[HARLogEntryResponseHeader]

    headers_size: float = FieldInfo(alias="headersSize")

    http_version: str = FieldInfo(alias="httpVersion")

    redirect_url: str = FieldInfo(alias="redirectURL")

    status: float

    status_text: str = FieldInfo(alias="statusText")


class HARLogEntry(BaseModel):
    initial_priority: str = FieldInfo(alias="_initialPriority")

    initiator_type: str = FieldInfo(alias="_initiator_type")

    priority: str = FieldInfo(alias="_priority")

    request_id: str = FieldInfo(alias="_requestId")

    request_time: float = FieldInfo(alias="_requestTime")

    resource_type: str = FieldInfo(alias="_resourceType")

    cache: object

    connection: str

    pageref: str

    request: HARLogEntryRequest

    response: HARLogEntryResponse

    server_ip_address: str = FieldInfo(alias="serverIPAddress")

    started_date_time: str = FieldInfo(alias="startedDateTime")

    time: float


class HARLogPagePageTimings(BaseModel):
    on_content_load: float = FieldInfo(alias="onContentLoad")

    on_load: float = FieldInfo(alias="onLoad")


class HARLogPage(BaseModel):
    id: str

    page_timings: HARLogPagePageTimings = FieldInfo(alias="pageTimings")

    started_date_time: str = FieldInfo(alias="startedDateTime")

    title: str


class HARLog(BaseModel):
    creator: HARLogCreator

    entries: List[HARLogEntry]

    pages: List[HARLogPage]

    version: str


class HAR(BaseModel):
    log: HARLog


class ScanHARResponse(BaseModel):
    har: HAR
