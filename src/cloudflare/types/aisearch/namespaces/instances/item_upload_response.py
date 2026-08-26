# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = ["ItemUploadResponse", "Warning", "WarningUnionMember0", "WarningUnionMember1"]


class WarningUnionMember0(BaseModel):
    code: Literal["custom_metadata_value_not_indexed"]

    expected_type: Literal["text", "number", "boolean", "datetime"]

    field: str


class WarningUnionMember1(BaseModel):
    code: Literal["custom_metadata_field_not_filterable"]

    field: str


Warning: TypeAlias = Union[WarningUnionMember0, WarningUnionMember1]


class ItemUploadResponse(BaseModel):
    id: str

    checksum: str

    chunks_count: Optional[int] = None

    created_at: datetime

    file_size: Optional[float] = None

    key: str

    last_seen_at: datetime

    metadata: Optional[Dict[str, Union[str, float, bool]]] = None
    """Built-in, configured filterable, and retained source metadata for the item."""

    namespace: str

    next_action: Optional[Literal["INDEX", "DELETE"]] = None

    source_id: Optional[str] = None
    """Identifies which data source this item belongs to.

    "builtin" for uploaded files, "{type}:{source}" for external sources, null for
    legacy items.
    """

    status: Literal["queued", "running", "completed", "error", "skipped", "outdated"]

    error: Optional[str] = None

    warnings: Optional[List[Warning]] = None
