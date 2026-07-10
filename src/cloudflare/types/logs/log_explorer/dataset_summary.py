# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DatasetSummary"]


class DatasetSummary(BaseModel):
    """A Log Explorer dataset summary.

    List endpoints return this type and omit
    field configuration; use the single-dataset endpoint to retrieve it.
    """

    created_at: datetime
    """RFC3339 timestamp recording when the API created this dataset."""

    dataset: str
    """Dataset type name (e.g. `http_requests`)."""

    dataset_id: str
    """Unique dataset ID."""

    enabled: bool
    """Whether log ingest is currently active for this dataset."""

    object_id: str
    """Public ID of the account or zone that owns this dataset."""

    object_type: Literal["account", "zone"]
    """Whether this dataset belongs to an account or a zone."""

    updated_at: datetime
    """RFC3339 timestamp recording when the API last updated this dataset."""
