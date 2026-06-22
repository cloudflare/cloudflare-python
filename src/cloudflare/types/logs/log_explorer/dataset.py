# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Dataset", "Field"]


class Field(BaseModel):
    enabled: bool
    """Whether the API includes this field in log ingest."""

    name: str
    """Field name in lowercase."""


class Dataset(BaseModel):
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

    fields: Optional[List[Field]] = None
    """The field configuration for this dataset."""
