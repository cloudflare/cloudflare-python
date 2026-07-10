# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AvailableDataset", "Schema"]


class Schema(BaseModel):
    """JSON Schema that describes the fields this dataset exposes."""

    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None

    type: Optional[Literal["object"]] = None


class AvailableDataset(BaseModel):
    """A dataset type that the account or zone can create."""

    dataset: str
    """Dataset type name (e.g. `http_requests`)."""

    object_type: Literal["account", "zone"]
    """Whether this dataset type is account-scoped or zone-scoped."""

    schema_: Schema = FieldInfo(alias="schema")
    """JSON Schema that describes the fields this dataset exposes."""

    timestamp_field: str
    """The primary timestamp field name for this dataset."""
