# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = [
    "PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse",
    "PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponseItem",
]


class PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponseItem(BaseModel):
    id: Optional[str] = None
    """UUID"""

    name: Optional[str] = None
    """The name of the pagerduty service."""


PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse = List[
    PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponseItem
]
