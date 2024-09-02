# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["D1Binding"]


class D1Binding(BaseModel):
    id: str
    """ID of the D1 database to bind to"""

    binding: str
    """A JavaScript variable name for the binding."""

    name: str
    """The name of the D1 database associated with the 'id' provided."""

    type: Literal["d1"]
    """The class of resource that the binding provides."""
