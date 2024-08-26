# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import List, Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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

    uploads: List[Upload]

    description: Optional[str] = None
    """The description of the dataset"""