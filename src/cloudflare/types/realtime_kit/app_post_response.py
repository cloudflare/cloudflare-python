# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AppPostResponse", "Data", "DataApp"]


class DataApp(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    app: Optional[DataApp] = None


class AppPostResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
