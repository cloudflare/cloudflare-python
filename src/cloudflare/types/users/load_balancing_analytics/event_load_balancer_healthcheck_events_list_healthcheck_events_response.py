# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse",
    "EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponseItem",
]


class EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponseItem(BaseModel):
    id: Optional[int] = None

    origins: Optional[List[object]] = None

    pool: Optional[object] = None

    timestamp: Optional[datetime] = None


EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse = List[
    EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponseItem
]
