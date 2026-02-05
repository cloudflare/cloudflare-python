# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AppGetResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    name: Optional[str] = None


class AppGetResponse(BaseModel):
    data: Optional[List[Data]] = None

    success: Optional[bool] = None
