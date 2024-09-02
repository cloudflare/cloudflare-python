# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Matcher"]


class Matcher(BaseModel):
    field: Literal["to"]
    """Field for type matcher."""

    type: Literal["literal"]
    """Type of matcher."""

    value: str
    """Value for matcher."""
