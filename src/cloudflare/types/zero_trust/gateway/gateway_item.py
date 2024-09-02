# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["GatewayItem"]


class GatewayItem(BaseModel):
    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the list item, if present"""

    value: Optional[str] = None
    """The value of the item in a list."""
