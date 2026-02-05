# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SinkCreateParams",
    "Config",
    "ConfigCloudflarePipelinesR2Table",
    "ConfigCloudflarePipelinesR2TableCredentials",
    "ConfigCloudflarePipelinesR2TableFileNaming",
    "ConfigCloudflarePipelinesR2TablePartitioning",
    "ConfigCloudflarePipelinesR2TableRollingPolicy",
    "ConfigCloudflarePipelinesR2DataCatalogTable",
    "ConfigCloudflarePipelinesR2DataCatalogTableRollingPolicy",
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


class SinkCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    name: Required[str]
    """Defines the name of the Sink."""

    type: Required[Literal["r2", "r2_data_catalog"]]
    """Specifies the type of sink."""

    config: Config
    """Defines the configuration of the R2 Sink."""

    format: Format

    schema: Schema


class ConfigCloudflarePipelinesR2TableCredentials(TypedDict, total=False):
    access_key_id: Required[str]
    """Cloudflare Account ID for the bucket"""

    secret_access_key: Required[str]
    """Cloudflare Account ID for the bucket"""


class ConfigCloudflarePipelinesR2TableFileNaming(TypedDict, total=False):
    """Controls filename prefix/suffix and strategy."""

    prefix: str
    """The prefix to use in file name. i.e prefix-<uuid>.parquet"""

    strategy: Literal["serial", "uuid", "uuid_v7", "ulid"]
    """Filename generation strategy."""

    suffix: str
    """This will overwrite the default file suffix. i.e .parquet, use with caution"""


class ConfigCloudflarePipelinesR2TablePartitioning(TypedDict, total=False):
    """Data-layout partitioning for sinks."""

    time_pattern: str
    """The pattern of the date string"""


class ConfigCloudflarePipelinesR2TableRollingPolicy(TypedDict, total=False):
    """Rolling policy for file sinks (when & why to close a file and open a new one)."""

    file_size_bytes: int
    """Files will be rolled after reaching this number of bytes"""

    inactivity_seconds: int
    """Number of seconds of inactivity to wait before rolling over to a new file"""

    interval_seconds: int
    """Number of seconds to wait before rolling over to a new file"""


class ConfigCloudflarePipelinesR2Table(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare Account ID for the bucket"""

    bucket: Required[str]
    """R2 Bucket to write to"""

    credentials: Required[ConfigCloudflarePipelinesR2TableCredentials]

    file_naming: ConfigCloudflarePipelinesR2TableFileNaming
    """Controls filename prefix/suffix and strategy."""

    jurisdiction: str
    """Jurisdiction this bucket is hosted in"""

    partitioning: ConfigCloudflarePipelinesR2TablePartitioning
    """Data-layout partitioning for sinks."""

    path: str
    """Subpath within the bucket to write to"""

    rolling_policy: ConfigCloudflarePipelinesR2TableRollingPolicy
    """Rolling policy for file sinks (when & why to close a file and open a new one)."""


class ConfigCloudflarePipelinesR2DataCatalogTableRollingPolicy(TypedDict, total=False):
    """Rolling policy for file sinks (when & why to close a file and open a new one)."""

    file_size_bytes: int
    """Files will be rolled after reaching this number of bytes"""

    inactivity_seconds: int
    """Number of seconds of inactivity to wait before rolling over to a new file"""

    interval_seconds: int
    """Number of seconds to wait before rolling over to a new file"""


class ConfigCloudflarePipelinesR2DataCatalogTable(TypedDict, total=False):
    """R2 Data Catalog Sink"""

    token: Required[str]
    """Authentication token"""

    account_id: Required[str]
    """Cloudflare Account ID"""

    bucket: Required[str]
    """The R2 Bucket that hosts this catalog"""

    table_name: Required[str]
    """Table name"""

    namespace: str
    """Table namespace"""

    rolling_policy: ConfigCloudflarePipelinesR2DataCatalogTableRollingPolicy
    """Rolling policy for file sinks (when & why to close a file and open a new one)."""


Config: TypeAlias = Union[ConfigCloudflarePipelinesR2Table, ConfigCloudflarePipelinesR2DataCatalogTable]


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
