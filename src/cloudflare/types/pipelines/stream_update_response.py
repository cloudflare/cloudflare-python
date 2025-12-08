# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["StreamUpdateResponse", "HTTP", "HTTPCORS", "WorkerBinding", "Format", "FormatJson", "FormatParquet"]


class HTTPCORS(BaseModel):
    """Specifies the CORS options for the HTTP endpoint."""

    origins: Optional[List[str]] = None


class HTTP(BaseModel):
    authentication: bool
    """Indicates that authentication is required for the HTTP endpoint."""

    enabled: bool
    """Indicates that the HTTP endpoint is enabled."""

    cors: Optional[HTTPCORS] = None
    """Specifies the CORS options for the HTTP endpoint."""


class WorkerBinding(BaseModel):
    enabled: bool
    """Indicates that the worker binding is enabled."""


class FormatJson(BaseModel):
    type: Literal["json"]

    decimal_encoding: Optional[Literal["number", "string", "bytes"]] = None

    timestamp_format: Optional[Literal["rfc3339", "unix_millis"]] = None

    unstructured: Optional[bool] = None


class FormatParquet(BaseModel):
    type: Literal["parquet"]

    compression: Optional[Literal["uncompressed", "snappy", "gzip", "zstd", "lz4"]] = None

    row_group_bytes: Optional[int] = None


Format: TypeAlias = Annotated[Union[FormatJson, FormatParquet], PropertyInfo(discriminator="type")]


class StreamUpdateResponse(BaseModel):
    id: str
    """Indicates a unique identifier for this stream."""

    created_at: datetime

    http: HTTP

    modified_at: datetime

    name: str
    """Indicates the name of the Stream."""

    version: int
    """Indicates the current version of this stream."""

    worker_binding: WorkerBinding

    endpoint: Optional[str] = None
    """Indicates the endpoint URL of this stream."""

    format: Optional[Format] = None
