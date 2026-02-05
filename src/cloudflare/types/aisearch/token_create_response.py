# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TokenCreateResponse"]


class TokenCreateResponse(BaseModel):
    id: str

    account_id: str

    account_tag: str

    cf_api_id: str

    cf_api_key: str

    created_at: datetime

    modified_at: datetime

    name: str

    created_by: Optional[str] = None

    enabled: Optional[bool] = None

    legacy: Optional[bool] = None

    modified_by: Optional[str] = None

    synced_at: Optional[datetime] = None
