# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["UploadCreateResponse", "Column"]


class Column(BaseModel):
    entry_id: str

    header_name: str

    num_cells: int

    upload_status: Literal["empty", "uploading", "pending", "processing", "failed", "complete"]


class UploadCreateResponse(BaseModel):
    encoding_version: int

    max_cells: int

    version: int

    case_sensitive: Optional[bool] = None

    columns: Optional[List[Column]] = None

    secret: Optional[str] = None
