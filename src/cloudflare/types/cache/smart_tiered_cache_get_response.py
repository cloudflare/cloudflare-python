# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SmartTieredCacheGetResponse"]


class SmartTieredCacheGetResponse(BaseModel):
    id: str
    """The identifier of the caching setting"""

    editable: bool
    """Whether the setting is editable"""

    modified_on: datetime
    """The time when the setting was last modified"""

    value: Literal["on", "off"]
    """The status of the feature being on / off"""
