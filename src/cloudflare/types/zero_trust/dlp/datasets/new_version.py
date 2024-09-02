# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing_extensions import Literal

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["NewVersion", "Column"]


class Column(BaseModel):
    entry_id: str

    header_name: str

    num_cells: int

    upload_status: Literal["empty", "uploading", "processing", "failed", "complete"]


class NewVersion(BaseModel):
    encoding_version: int

    max_cells: int

    version: int

    columns: Optional[List[Column]] = None

    secret: Optional[str] = None
