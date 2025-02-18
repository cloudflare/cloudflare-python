# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HistoryListResponse"]


class HistoryListResponse(BaseModel):
    id: int
    """ID of the configuration"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Date and time the configuration was created"""

    description: str
    """Configuration description provided by the user who published this configuration"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Date and time the configuration was last updated"""

    user_id: str = FieldInfo(alias="userId")
    """Alpha-numeric ID of the account user who published the configuration"""
