# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "StreamGetResponse",
    "HTTP",
    "HTTPCORS",
    "WorkerBinding",
    "Format",
    "FormatJson",
    "FormatParquet",
    "Schema",
    "SchemaField",
    "SchemaFieldInt32",
    "SchemaFieldInt64",
    "SchemaFieldFloat32",
    "SchemaFieldFloat64",
    "SchemaFieldBool",
    "SchemaFieldString",
    "SchemaFieldBinary",
    "SchemaFieldTimestamp",
    "SchemaFieldJson",
    "SchemaFieldStruct",
    "SchemaFieldList",
    "SchemaFormat",
    "SchemaFormatJson",
    "SchemaFormatParquet",
]


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


class SchemaFieldInt32(BaseModel):
    type: Literal["int32"]

    metadata_key: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    sql_name: Optional[str] = None


class SchemaFieldInt64(BaseModel):
    type: Literal["int64"]

    metadata_key: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    sql_name: Optional[str] = None


class SchemaFieldFloat32(BaseModel):
    type: Literal["float32"]

    metadata_key: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    sql_name: Optional[str] = None


class SchemaFieldFloat64(BaseModel):
    type: Literal["float64"]

    metadata_key: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    sql_name: Optional[str] = None


class SchemaFieldBool(BaseModel):
    type: Literal["bool"]

    metadata_key: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    sql_name: Optional[str] = None


class SchemaFieldString(BaseModel):
    type: Literal["string"]

    metadata_key: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    sql_name: Optional[str] = None


class SchemaFieldBinary(BaseModel):
    type: Literal["binary"]

    metadata_key: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    sql_name: Optional[str] = None


class SchemaFieldTimestamp(BaseModel):
    type: Literal["timestamp"]

    metadata_key: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    sql_name: Optional[str] = None

    unit: Optional[Literal["second", "millisecond", "microsecond", "nanosecond"]] = None


class SchemaFieldJson(BaseModel):
    type: Literal["json"]

    metadata_key: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    sql_name: Optional[str] = None


class SchemaFieldStruct:
    pass


class SchemaFieldList:
    pass


SchemaField: TypeAlias = Annotated[
    Union[
        SchemaFieldInt32,
        SchemaFieldInt64,
        SchemaFieldFloat32,
        SchemaFieldFloat64,
        SchemaFieldBool,
        SchemaFieldString,
        SchemaFieldBinary,
        SchemaFieldTimestamp,
        SchemaFieldJson,
        SchemaFieldStruct,
        SchemaFieldList,
    ],
    PropertyInfo(discriminator="type"),
]


class SchemaFormatJson(BaseModel):
    type: Literal["json"]

    decimal_encoding: Optional[Literal["number", "string", "bytes"]] = None

    timestamp_format: Optional[Literal["rfc3339", "unix_millis"]] = None

    unstructured: Optional[bool] = None


class SchemaFormatParquet(BaseModel):
    type: Literal["parquet"]

    compression: Optional[Literal["uncompressed", "snappy", "gzip", "zstd", "lz4"]] = None

    row_group_bytes: Optional[int] = None


SchemaFormat: TypeAlias = Annotated[Union[SchemaFormatJson, SchemaFormatParquet], PropertyInfo(discriminator="type")]


class Schema(BaseModel):
    fields: Optional[List[SchemaField]] = None

    format: Optional[SchemaFormat] = None

    inferred: Optional[bool] = None


class StreamGetResponse(BaseModel):
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

    schema_: Optional[Schema] = FieldInfo(alias="schema", default=None)
