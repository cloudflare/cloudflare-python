# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IndicatorFeedGetResponse"]


class IndicatorFeedGetResponse(BaseModel):
    id: Optional[int] = None
    """The unique identifier for the indicator feed"""

    created_on: Optional[datetime] = None
    """The date and time when the data entry was created"""

    description: Optional[str] = None
    """The description of the example test"""

    latest_upload_status: Optional[
        Literal["Mirroring", "Unifying", "Loading", "Provisioning", "Complete", "Error"]
    ] = None
    """Status of the latest snapshot uploaded"""

    modified_on: Optional[datetime] = None
    """The date and time when the data entry was last modified"""

    name: Optional[str] = None
    """The name of the indicator feed"""
