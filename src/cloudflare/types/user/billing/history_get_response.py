# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["HistoryGetResponse", "HistoryGetResponseItem", "HistoryGetResponseItemZone"]


class HistoryGetResponseItemZone(BaseModel):
    name: Optional[object] = None


class HistoryGetResponseItem(BaseModel):
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

    zone: HistoryGetResponseItemZone


HistoryGetResponse = List[HistoryGetResponseItem]
