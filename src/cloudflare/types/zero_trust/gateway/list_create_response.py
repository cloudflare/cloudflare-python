# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .gateway_item import GatewayItem

__all__ = ["ListCreateResponse"]


class ListCreateResponse(BaseModel):
    id: Optional[str] = None
    """Identify the API resource with a UUID."""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Provide the list description."""

    items: Optional[List[GatewayItem]] = None
    """Provide the list items."""

    name: Optional[str] = None
    """Specify the list name."""

    type: Optional[Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"]] = None
    """Specify the list type."""

    updated_at: Optional[datetime] = None
