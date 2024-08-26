# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SubscriptionComponent"]

class SubscriptionComponent(BaseModel):
    default: Optional[float] = None
    """The default amount assigned."""

    name: Optional[str] = None
    """The name of the component value."""

    price: Optional[float] = None
    """The unit price for the component value."""

    value: Optional[float] = None
    """The amount of the component value assigned."""