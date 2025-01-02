# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["AssetCreateResponse"]


class AssetCreateResponse(BaseModel):
    id: str

    bucket_name: str

    created_at: datetime

    file_name: str

    finetune_id: str

    modified_at: datetime
