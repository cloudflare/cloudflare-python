# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["EntryCreateResponse"]


class EntryCreateResponse(BaseModel):
    entry_id: str

    header_name: str

    num_cells: int

    upload_status: Literal["empty", "uploading", "processing", "failed", "complete"]
