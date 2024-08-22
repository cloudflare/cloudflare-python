# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["BillingHistory", "Zone"]

class Zone(BaseModel):
    name: Optional[str] = None

class BillingHistory(BaseModel):
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

    zone: Zone