# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "PipelineUpdateParams",
    "Destination",
    "DestinationBatch",
    "DestinationCompression",
    "DestinationPath",
    "DestinationCredentials",
    "Source",
    "SourceCloudflarePipelinesWorkersPipelinesHTTPSource",
    "SourceCloudflarePipelinesWorkersPipelinesHTTPSourceCORS",
    "SourceCloudflarePipelinesWorkersPipelinesBindingSource",
]


class PipelineUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    destination: Required[Destination]

    name: Required[str]
    """Defines the name of the pipeline."""

    source: Required[Iterable[Source]]


class DestinationBatch(TypedDict, total=False):
    max_bytes: int
    """Specifies rough maximum size of files."""

    max_duration_s: float
    """Specifies duration to wait to aggregate batches files."""

    max_rows: int
    """Specifies rough maximum number of rows per file."""


class DestinationCompression(TypedDict, total=False):
    type: Literal["none", "gzip", "deflate"]
    """Specifies the desired compression algorithm and format."""


class DestinationPath(TypedDict, total=False):
    bucket: Required[str]
    """Specifies the R2 Bucket to store files."""

    filename: str
    """Specifies the name pattern to for individual data files."""

    filepath: str
    """Specifies the name pattern for directory."""

    prefix: str
    """Specifies the base directory within the bucket."""


class DestinationCredentials(TypedDict, total=False):
    access_key_id: Required[str]
    """Specifies the R2 Bucket Access Key Id."""

    endpoint: Required[str]
    """Specifies the R2 Endpoint."""

    secret_access_key: Required[str]
    """Specifies the R2 Bucket Secret Access Key."""


class Destination(TypedDict, total=False):
    batch: Required[DestinationBatch]

    compression: Required[DestinationCompression]

    format: Required[Literal["json"]]
    """Specifies the format of data to deliver."""

    path: Required[DestinationPath]

    type: Required[Literal["r2"]]
    """Specifies the type of destination."""

    credentials: DestinationCredentials


class SourceCloudflarePipelinesWorkersPipelinesHTTPSourceCORS(TypedDict, total=False):
    origins: List[str]
    """Specifies allowed origins to allow Cross Origin HTTP Requests."""


class SourceCloudflarePipelinesWorkersPipelinesHTTPSource(TypedDict, total=False):
    format: Required[Literal["json"]]
    """Specifies the format of source data."""

    type: Required[str]

    authentication: bool
    """Specifies whether authentication is required to send to this pipeline via HTTP."""

    cors: SourceCloudflarePipelinesWorkersPipelinesHTTPSourceCORS


class SourceCloudflarePipelinesWorkersPipelinesBindingSource(TypedDict, total=False):
    format: Required[Literal["json"]]
    """Specifies the format of source data."""

    type: Required[str]


Source: TypeAlias = Union[
    SourceCloudflarePipelinesWorkersPipelinesHTTPSource, SourceCloudflarePipelinesWorkersPipelinesBindingSource
]
