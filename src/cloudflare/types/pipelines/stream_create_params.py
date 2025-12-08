# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "StreamCreateParams",
    "Format",
    "FormatJson",
    "FormatParquet",
    "HTTP",
    "HTTPCORS",
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
    "WorkerBinding",
]


class StreamCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    name: Required[str]
    """Specifies the name of the Stream."""

    format: Format

    http: HTTP

    schema: Schema

    worker_binding: WorkerBinding


class FormatJson(TypedDict, total=False):
    type: Required[Literal["json"]]

    decimal_encoding: Literal["number", "string", "bytes"]

    timestamp_format: Literal["rfc3339", "unix_millis"]

    unstructured: bool


class FormatParquet(TypedDict, total=False):
    type: Required[Literal["parquet"]]

    compression: Literal["uncompressed", "snappy", "gzip", "zstd", "lz4"]

    row_group_bytes: Optional[int]


Format: TypeAlias = Union[FormatJson, FormatParquet]


class HTTPCORS(TypedDict, total=False):
    """Specifies the CORS options for the HTTP endpoint."""

    origins: SequenceNotStr[str]


class HTTP(TypedDict, total=False):
    authentication: Required[bool]
    """Indicates that authentication is required for the HTTP endpoint."""

    enabled: Required[bool]
    """Indicates that the HTTP endpoint is enabled."""

    cors: HTTPCORS
    """Specifies the CORS options for the HTTP endpoint."""


class SchemaFieldInt32(TypedDict, total=False):
    type: Required[Literal["int32"]]

    metadata_key: Optional[str]

    name: str

    required: bool

    sql_name: str


class SchemaFieldInt64(TypedDict, total=False):
    type: Required[Literal["int64"]]

    metadata_key: Optional[str]

    name: str

    required: bool

    sql_name: str


class SchemaFieldFloat32(TypedDict, total=False):
    type: Required[Literal["float32"]]

    metadata_key: Optional[str]

    name: str

    required: bool

    sql_name: str


class SchemaFieldFloat64(TypedDict, total=False):
    type: Required[Literal["float64"]]

    metadata_key: Optional[str]

    name: str

    required: bool

    sql_name: str


class SchemaFieldBool(TypedDict, total=False):
    type: Required[Literal["bool"]]

    metadata_key: Optional[str]

    name: str

    required: bool

    sql_name: str


class SchemaFieldString(TypedDict, total=False):
    type: Required[Literal["string"]]

    metadata_key: Optional[str]

    name: str

    required: bool

    sql_name: str


class SchemaFieldBinary(TypedDict, total=False):
    type: Required[Literal["binary"]]

    metadata_key: Optional[str]

    name: str

    required: bool

    sql_name: str


class SchemaFieldTimestamp(TypedDict, total=False):
    type: Required[Literal["timestamp"]]

    metadata_key: Optional[str]

    name: str

    required: bool

    sql_name: str

    unit: Literal["second", "millisecond", "microsecond", "nanosecond"]


class SchemaFieldJson(TypedDict, total=False):
    type: Required[Literal["json"]]

    metadata_key: Optional[str]

    name: str

    required: bool

    sql_name: str


class SchemaFieldStruct(total=False):
    pass


class SchemaFieldList(total=False):
    pass


SchemaField: TypeAlias = Union[
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
]


class SchemaFormatJson(TypedDict, total=False):
    type: Required[Literal["json"]]

    decimal_encoding: Literal["number", "string", "bytes"]

    timestamp_format: Literal["rfc3339", "unix_millis"]

    unstructured: bool


class SchemaFormatParquet(TypedDict, total=False):
    type: Required[Literal["parquet"]]

    compression: Literal["uncompressed", "snappy", "gzip", "zstd", "lz4"]

    row_group_bytes: Optional[int]


SchemaFormat: TypeAlias = Union[SchemaFormatJson, SchemaFormatParquet]


class Schema(TypedDict, total=False):
    fields: Iterable[SchemaField]

    format: SchemaFormat

    inferred: Optional[bool]


class WorkerBinding(TypedDict, total=False):
    enabled: Required[bool]
    """Indicates that the worker binding is enabled."""
