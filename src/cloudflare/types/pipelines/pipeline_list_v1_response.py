# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PipelineListV1Response"]


class PipelineListV1Response(BaseModel):
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
