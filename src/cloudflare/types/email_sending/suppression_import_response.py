# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SuppressionImportResponse", "Item"]


class Item(BaseModel):
    index: int

    status: Literal["processed", "invalid", "error", "skipped"]

    id: Optional[str] = None

    email: Optional[str] = None

    error: Optional[str] = None


class SuppressionImportResponse(BaseModel):
    deduplicated: int

    errors: int

    invalid: int

    items: List[Item]

    processed: int

    skipped: int

    total: int
