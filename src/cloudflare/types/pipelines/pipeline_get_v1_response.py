# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PipelineGetV1Response", "Table"]


class Table(BaseModel):
    id: str
    """Unique identifier for the connection (stream or sink)."""

    latest: int
    """Latest available version of the connection."""

    name: str
    """Name of the connection."""

    type: Literal["stream", "sink"]
    """Type of the connection."""

    version: int
    """Current version of the connection used by this pipeline."""


class PipelineGetV1Response(BaseModel):
    id: str
    """Indicates a unique identifier for this pipeline."""

    created_at: str

    modified_at: str

    name: str
    """Indicates the name of the Pipeline."""

    sql: str
    """Specifies SQL for the Pipeline processing flow."""

    status: str
    """Indicates the current status of the Pipeline."""

    tables: List[Table]
    """List of streams and sinks used by this pipeline."""
