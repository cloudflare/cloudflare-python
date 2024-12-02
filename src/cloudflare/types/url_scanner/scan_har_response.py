# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ScanHARResponse",
    "Log",
    "LogCreator",
    "LogEntry",
    "LogEntryRequest",
    "LogEntryRequestHeader",
    "LogEntryResponse",
    "LogEntryResponseContent",
    "LogEntryResponseHeader",
    "LogPage",
    "LogPagePageTimings",
]


class LogCreator(BaseModel):
    comment: str

    name: str

    version: str


class LogEntryRequestHeader(BaseModel):
    name: str

    value: str


class LogEntryRequest(BaseModel):
    body_size: float = FieldInfo(alias="bodySize")

    headers: List[LogEntryRequestHeader]

    headers_size: float = FieldInfo(alias="headersSize")

    http_version: str = FieldInfo(alias="httpVersion")

    method: str

    url: str


class LogEntryResponseContent(BaseModel):
    mime_type: str = FieldInfo(alias="mimeType")

    size: float

    compression: Optional[int] = None


class LogEntryResponseHeader(BaseModel):
    name: str

    value: str


class LogEntryResponse(BaseModel):
    transfer_size: float = FieldInfo(alias="_transferSize")

    body_size: float = FieldInfo(alias="bodySize")

    content: LogEntryResponseContent

    headers: List[LogEntryResponseHeader]

    headers_size: float = FieldInfo(alias="headersSize")

    http_version: str = FieldInfo(alias="httpVersion")

    redirect_url: str = FieldInfo(alias="redirectURL")

    status: float

    status_text: str = FieldInfo(alias="statusText")


class LogEntry(BaseModel):
    initial_priority: str = FieldInfo(alias="_initialPriority")

    initiator_type: str = FieldInfo(alias="_initiator_type")

    priority: str = FieldInfo(alias="_priority")

    request_id: str = FieldInfo(alias="_requestId")

    request_time: float = FieldInfo(alias="_requestTime")

    resource_type: str = FieldInfo(alias="_resourceType")

    cache: object

    connection: str

    pageref: str

    request: LogEntryRequest

    response: LogEntryResponse

    server_ip_address: str = FieldInfo(alias="serverIPAddress")

    started_date_time: str = FieldInfo(alias="startedDateTime")

    time: float


class LogPagePageTimings(BaseModel):
    on_content_load: float = FieldInfo(alias="onContentLoad")

    on_load: float = FieldInfo(alias="onLoad")


class LogPage(BaseModel):
    id: str

    page_timings: LogPagePageTimings = FieldInfo(alias="pageTimings")

    started_date_time: str = FieldInfo(alias="startedDateTime")

    title: str


class Log(BaseModel):
    creator: LogCreator

    entries: List[LogEntry]

    pages: List[LogPage]

    version: str


class ScanHARResponse(BaseModel):
    log: Log
