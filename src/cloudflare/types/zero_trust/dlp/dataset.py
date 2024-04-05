# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Dataset", "Upload"]


class Upload(BaseModel):
    num_cells: int

    status: Literal["empty", "uploading", "failed", "complete"]

    version: int


class Dataset(BaseModel):
    id: str

    created_at: datetime

    name: str

    num_cells: int

    secret: bool

    status: Literal["empty", "uploading", "failed", "complete"]

    updated_at: datetime

    uploads: List[Upload]

    description: Optional[str] = None
