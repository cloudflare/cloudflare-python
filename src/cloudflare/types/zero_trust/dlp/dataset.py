# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Dataset", "Column", "Upload"]


class Column(BaseModel):
    entry_id: str

    header_name: str

    num_cells: int

    upload_status: Literal["empty", "uploading", "processing", "failed", "complete"]


class Upload(BaseModel):
    num_cells: int

    status: Literal["empty", "uploading", "processing", "failed", "complete"]

    version: int


class Dataset(BaseModel):
    id: str

    columns: List[Column]

    created_at: datetime

    encoding_version: int

    name: str

    num_cells: int

    secret: bool

    status: Literal["empty", "uploading", "processing", "failed", "complete"]

    updated_at: datetime
    """When the dataset was last updated.

    This includes name or description changes as well as uploads.
    """

    uploads: List[Upload]

    description: Optional[str] = None
    """The description of the dataset"""
