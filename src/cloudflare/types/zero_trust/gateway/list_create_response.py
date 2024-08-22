# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from datetime import datetime

from .gateway_item import GatewayItem

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ListCreateResponse"]

class ListCreateResponse(BaseModel):
    id: Optional[str] = None
    """API Resource UUID tag."""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the list."""

    items: Optional[List[GatewayItem]] = None
    """The items in the list."""

    name: Optional[str] = None
    """The name of the list."""

    type: Optional[Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"]] = None
    """The type of list."""

    updated_at: Optional[datetime] = None