# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "ScanHarResponse",
    "Har",
    "HarLog",
    "HarLogCreator",
    "HarLogEntry",
    "HarLogEntryRequest",
    "HarLogEntryRequestHeader",
    "HarLogEntryResponse",
    "HarLogEntryResponseContent",
    "HarLogEntryResponseHeader",
    "HarLogPage",
    "HarLogPagePageTimings",
]


class HarLogCreator(BaseModel):
    comment: str

    name: str

    version: str


class HarLogEntryRequestHeader(BaseModel):
    name: str

    value: str


class HarLogEntryRequest(BaseModel):
    body_size: float = FieldInfo(alias="bodySize")

    headers: List[HarLogEntryRequestHeader]

    headers_size: float = FieldInfo(alias="headersSize")

    http_version: str = FieldInfo(alias="httpVersion")

    method: str

    url: str


class HarLogEntryResponseContent(BaseModel):
    mime_type: str = FieldInfo(alias="mimeType")

    size: float

    compression: Optional[int] = None


class HarLogEntryResponseHeader(BaseModel):
    name: str

    value: str


class HarLogEntryResponse(BaseModel):
    api_transfer_size: float = FieldInfo(alias="_transferSize")

    body_size: float = FieldInfo(alias="bodySize")

    content: HarLogEntryResponseContent

    headers: List[HarLogEntryResponseHeader]

    headers_size: float = FieldInfo(alias="headersSize")

    http_version: str = FieldInfo(alias="httpVersion")

    redirect_url: str = FieldInfo(alias="redirectURL")

    status: float

    status_text: str = FieldInfo(alias="statusText")


class HarLogEntry(BaseModel):
    api_initial_priority: str = FieldInfo(alias="_initialPriority")

    api_initiator_type: str = FieldInfo(alias="_initiator_type")

    api_priority: str = FieldInfo(alias="_priority")

    api_request_id: str = FieldInfo(alias="_requestId")

    api_request_time: float = FieldInfo(alias="_requestTime")

    api_resource_type: str = FieldInfo(alias="_resourceType")

    cache: object

    connection: str

    pageref: str

    request: HarLogEntryRequest

    response: HarLogEntryResponse

    server_ip_address: str = FieldInfo(alias="serverIPAddress")

    started_date_time: str = FieldInfo(alias="startedDateTime")

    time: float


class HarLogPagePageTimings(BaseModel):
    on_content_load: float = FieldInfo(alias="onContentLoad")

    on_load: float = FieldInfo(alias="onLoad")


class HarLogPage(BaseModel):
    id: str

    page_timings: HarLogPagePageTimings = FieldInfo(alias="pageTimings")

    started_date_time: str = FieldInfo(alias="startedDateTime")

    title: str


class HarLog(BaseModel):
    creator: HarLogCreator

    entries: List[HarLogEntry]

    pages: List[HarLogPage]

    version: str


class Har(BaseModel):
    log: HarLog


class ScanHarResponse(BaseModel):
    har: Har
