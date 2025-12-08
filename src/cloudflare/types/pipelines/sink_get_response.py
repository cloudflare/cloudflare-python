# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "SinkGetResponse",
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


class ConfigCloudflarePipelinesR2TableCredentials(BaseModel):
    access_key_id: str
    """Cloudflare Account ID for the bucket"""

    secret_access_key: str
    """Cloudflare Account ID for the bucket"""


class ConfigCloudflarePipelinesR2TableFileNaming(BaseModel):
    """Controls filename prefix/suffix and strategy."""

    prefix: Optional[str] = None
    """The prefix to use in file name. i.e prefix-<uuid>.parquet"""

    strategy: Optional[Literal["serial", "uuid", "uuid_v7", "ulid"]] = None
    """Filename generation strategy."""

    suffix: Optional[str] = None
    """This will overwrite the default file suffix. i.e .parquet, use with caution"""


class ConfigCloudflarePipelinesR2TablePartitioning(BaseModel):
    """Data-layout partitioning for sinks."""

    time_pattern: Optional[str] = None
    """The pattern of the date string"""


class ConfigCloudflarePipelinesR2TableRollingPolicy(BaseModel):
    """Rolling policy for file sinks (when & why to close a file and open a new one)."""

    file_size_bytes: Optional[int] = None
    """Files will be rolled after reaching this number of bytes"""

    inactivity_seconds: Optional[int] = None
    """Number of seconds of inactivity to wait before rolling over to a new file"""

    interval_seconds: Optional[int] = None
    """Number of seconds to wait before rolling over to a new file"""


class ConfigCloudflarePipelinesR2Table(BaseModel):
    account_id: str
    """Cloudflare Account ID for the bucket"""

    bucket: str
    """R2 Bucket to write to"""

    credentials: ConfigCloudflarePipelinesR2TableCredentials

    file_naming: Optional[ConfigCloudflarePipelinesR2TableFileNaming] = None
    """Controls filename prefix/suffix and strategy."""

    jurisdiction: Optional[str] = None
    """Jurisdiction this bucket is hosted in"""

    partitioning: Optional[ConfigCloudflarePipelinesR2TablePartitioning] = None
    """Data-layout partitioning for sinks."""

    path: Optional[str] = None
    """Subpath within the bucket to write to"""

    rolling_policy: Optional[ConfigCloudflarePipelinesR2TableRollingPolicy] = None
    """Rolling policy for file sinks (when & why to close a file and open a new one)."""


class ConfigCloudflarePipelinesR2DataCatalogTableRollingPolicy(BaseModel):
    """Rolling policy for file sinks (when & why to close a file and open a new one)."""

    file_size_bytes: Optional[int] = None
    """Files will be rolled after reaching this number of bytes"""

    inactivity_seconds: Optional[int] = None
    """Number of seconds of inactivity to wait before rolling over to a new file"""

    interval_seconds: Optional[int] = None
    """Number of seconds to wait before rolling over to a new file"""


class ConfigCloudflarePipelinesR2DataCatalogTable(BaseModel):
    """R2 Data Catalog Sink"""

    token: str
    """Authentication token"""

    account_id: str
    """Cloudflare Account ID"""

    bucket: str
    """The R2 Bucket that hosts this catalog"""

    table_name: str
    """Table name"""

    namespace: Optional[str] = None
    """Table namespace"""

    rolling_policy: Optional[ConfigCloudflarePipelinesR2DataCatalogTableRollingPolicy] = None
    """Rolling policy for file sinks (when & why to close a file and open a new one)."""


Config: TypeAlias = Union[ConfigCloudflarePipelinesR2Table, ConfigCloudflarePipelinesR2DataCatalogTable]


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


class SinkGetResponse(BaseModel):
    id: str
    """Indicates a unique identifier for this sink."""

    created_at: datetime

    modified_at: datetime

    name: str
    """Defines the name of the Sink."""

    type: Literal["r2", "r2_data_catalog"]
    """Specifies the type of sink."""

    config: Optional[Config] = None
    """Defines the configuration of the R2 Sink."""

    format: Optional[Format] = None

    schema_: Optional[Schema] = FieldInfo(alias="schema", default=None)
