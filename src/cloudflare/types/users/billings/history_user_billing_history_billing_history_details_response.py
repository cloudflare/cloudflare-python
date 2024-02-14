# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "HistoryUserBillingHistoryBillingHistoryDetailsResponse",
    "HistoryUserBillingHistoryBillingHistoryDetailsResponseItem",
    "HistoryUserBillingHistoryBillingHistoryDetailsResponseItemZone",
]


class HistoryUserBillingHistoryBillingHistoryDetailsResponseItemZone(BaseModel):
    name: Optional[object] = None


class HistoryUserBillingHistoryBillingHistoryDetailsResponseItem(BaseModel):
    id: str
    """Billing item identifier tag."""

    action: str
    """The billing item action."""

    amount: float
    """The amount associated with this billing item."""

    currency: str
    """The monetary unit in which pricing information is displayed."""

    description: str
    """The billing item description."""

    occurred_at: datetime
    """When the billing item was created."""

    type: str
    """The billing item type."""

    zone: HistoryUserBillingHistoryBillingHistoryDetailsResponseItemZone


HistoryUserBillingHistoryBillingHistoryDetailsResponse = List[
    HistoryUserBillingHistoryBillingHistoryDetailsResponseItem
]
