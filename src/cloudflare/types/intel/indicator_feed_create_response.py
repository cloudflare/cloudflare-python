# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["IndicatorFeedCreateResponse"]


class IndicatorFeedCreateResponse(BaseModel):
    id: Optional[int] = None
    """The unique identifier for the indicator feed"""

    created_on: Optional[datetime] = None
    """The date and time when the data entry was created"""

    description: Optional[str] = None
    """The description of the example test"""

    is_attributable: Optional[bool] = None
    """Whether the indicator feed can be attributed to a provider"""

    is_downloadable: Optional[bool] = None
    """Whether the indicator feed can be downloaded"""

    is_public: Optional[bool] = None
    """Whether the indicator feed is exposed to customers"""

    modified_on: Optional[datetime] = None
    """The date and time when the data entry was last modified"""

    name: Optional[str] = None
    """The name of the indicator feed"""
