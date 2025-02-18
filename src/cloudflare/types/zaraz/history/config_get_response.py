# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..configuration import Configuration

__all__ = ["ConfigGetResponse", "ConfigGetResponseItem"]


class ConfigGetResponseItem(BaseModel):
    id: int
    """ID of the configuration"""

    config: Configuration
    """Zaraz configuration"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Date and time the configuration was created"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Date and time the configuration was last updated"""

    user_id: str = FieldInfo(alias="userId")
    """Alpha-numeric ID of the account user who published the configuration"""


ConfigGetResponse: TypeAlias = Dict[str, ConfigGetResponseItem]
