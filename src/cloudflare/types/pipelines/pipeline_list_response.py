# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "PipelineListResponse",
    "ResultInfo",
    "Result",
    "ResultDestination",
    "ResultDestinationBatch",
    "ResultDestinationCompression",
    "ResultDestinationPath",
    "ResultSource",
    "ResultSourceCloudflarePipelinesWorkersPipelinesHTTPSource",
    "ResultSourceCloudflarePipelinesWorkersPipelinesHTTPSourceCORS",
    "ResultSourceCloudflarePipelinesWorkersPipelinesBindingSource",
]


class ResultInfo(BaseModel):
    count: float
    """Indicates the number of items on current page."""

    page: float
    """Indicates the current page number."""

    per_page: float
    """Indicates the number of items per page."""

    total_count: float
    """Indicates the total number of items."""


class ResultDestinationBatch(BaseModel):
    max_bytes: int
    """Specifies rough maximum size of files."""

    max_duration_s: float
    """Specifies duration to wait to aggregate batches files."""

    max_rows: int
    """Specifies rough maximum number of rows per file."""


class ResultDestinationCompression(BaseModel):
    type: Literal["none", "gzip", "deflate"]
    """Specifies the desired compression algorithm and format."""


class ResultDestinationPath(BaseModel):
    bucket: str
    """Specifies the R2 Bucket to store files."""

    filename: Optional[str] = None
    """Specifies the name pattern to for individual data files."""

    filepath: Optional[str] = None
    """Specifies the name pattern for directory."""

    prefix: Optional[str] = None
    """Specifies the base directory within the bucket."""


class ResultDestination(BaseModel):
    batch: ResultDestinationBatch

    compression: ResultDestinationCompression

    format: Literal["json"]
    """Specifies the format of data to deliver."""

    path: ResultDestinationPath

    type: Literal["r2"]
    """Specifies the type of destination."""


class ResultSourceCloudflarePipelinesWorkersPipelinesHTTPSourceCORS(BaseModel):
    origins: Optional[List[str]] = None
    """Specifies allowed origins to allow Cross Origin HTTP Requests."""


class ResultSourceCloudflarePipelinesWorkersPipelinesHTTPSource(BaseModel):
    format: Literal["json"]
    """Specifies the format of source data."""

    type: str

    authentication: Optional[bool] = None
    """Specifies whether authentication is required to send to this pipeline via HTTP."""

    cors: Optional[ResultSourceCloudflarePipelinesWorkersPipelinesHTTPSourceCORS] = None


class ResultSourceCloudflarePipelinesWorkersPipelinesBindingSource(BaseModel):
    format: Literal["json"]
    """Specifies the format of source data."""

    type: str


ResultSource: TypeAlias = Union[
    ResultSourceCloudflarePipelinesWorkersPipelinesHTTPSource,
    ResultSourceCloudflarePipelinesWorkersPipelinesBindingSource,
]


class Result(BaseModel):
    id: str
    """Specifies the pipeline identifier."""

    destination: ResultDestination

    endpoint: str
    """Indicates the endpoint URL to send traffic."""

    name: str
    """Defines the name of the pipeline."""

    source: List[ResultSource]

    version: float
    """Indicates the version number of last saved configuration."""


class PipelineListResponse(BaseModel):
    result_info: ResultInfo

    results: List[Result]

    success: bool
    """Indicates whether the API call was successful."""
