# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = ["VersionCreateResponse", "VersionCreateResponseItem"]


class VersionCreateResponseItem(BaseModel):
    entry_id: str

    header_name: str

    num_cells: int

    upload_status: Literal["empty", "uploading", "processing", "failed", "complete"]


VersionCreateResponse: TypeAlias = List[VersionCreateResponseItem]
