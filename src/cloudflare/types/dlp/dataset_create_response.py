# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from datetime import datetime

from typing import List, Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["DatasetCreateResponse", "Dataset", "DatasetUpload"]


class DatasetUpload(BaseModel):
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

    uploads: List[DatasetUpload]

    description: Optional[str] = None


class DatasetCreateResponse(BaseModel):
    dataset: Dataset

    max_cells: int

    version: int
    """The version to use when uploading the dataset."""

    secret: Optional[str] = None
    """The secret to use for Exact Data Match datasets.

    This is not present in Custom Wordlists.
    """
