# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "PipelineGetResponse",
    "Destination",
    "DestinationBatch",
    "DestinationCompression",
    "DestinationPath",
    "Source",
    "SourceCloudflarePipelinesWorkersPipelinesHTTPSource",
    "SourceCloudflarePipelinesWorkersPipelinesHTTPSourceCORS",
    "SourceCloudflarePipelinesWorkersPipelinesBindingSource",
]


class DestinationBatch(BaseModel):
    max_bytes: int
    """Specifies rough maximum size of files."""

    max_duration_s: float
    """Specifies duration to wait to aggregate batches files."""

    max_rows: int
    """Specifies rough maximum number of rows per file."""


class DestinationCompression(BaseModel):
    type: Literal["none", "gzip", "deflate"]
    """Specifies the desired compression algorithm and format."""


class DestinationPath(BaseModel):
    bucket: str
    """Specifies the R2 Bucket to store files."""

    filename: Optional[str] = None
    """Specifies the name pattern to for individual data files."""

    filepath: Optional[str] = None
    """Specifies the name pattern for directory."""

    prefix: Optional[str] = None
    """Specifies the base directory within the bucket."""


class Destination(BaseModel):
    batch: DestinationBatch

    compression: DestinationCompression

    format: Literal["json"]
    """Specifies the format of data to deliver."""

    path: DestinationPath

    type: Literal["r2"]
    """Specifies the type of destination."""


class SourceCloudflarePipelinesWorkersPipelinesHTTPSourceCORS(BaseModel):
    origins: Optional[List[str]] = None
    """Specifies allowed origins to allow Cross Origin HTTP Requests."""


class SourceCloudflarePipelinesWorkersPipelinesHTTPSource(BaseModel):
    format: Literal["json"]
    """Specifies the format of source data."""

    type: str

    authentication: Optional[bool] = None
    """Specifies whether authentication is required to send to this pipeline via HTTP."""

    cors: Optional[SourceCloudflarePipelinesWorkersPipelinesHTTPSourceCORS] = None


class SourceCloudflarePipelinesWorkersPipelinesBindingSource(BaseModel):
    format: Literal["json"]
    """Specifies the format of source data."""

    type: str


Source: TypeAlias = Union[
    SourceCloudflarePipelinesWorkersPipelinesHTTPSource, SourceCloudflarePipelinesWorkersPipelinesBindingSource
]


class PipelineGetResponse(BaseModel):
    id: str
    """Specifies the pipeline identifier."""

    destination: Destination

    endpoint: str
    """Indicates the endpoint URL to send traffic."""

    name: str
    """Defines the name of the pipeline."""

    source: List[Source]

    version: float
    """Indicates the version number of last saved configuration."""
