# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RewriteURIPart", "StaticValue", "DynamicValue"]


class StaticValue(BaseModel):
    value: str
    """Predefined replacement value."""


class DynamicValue(BaseModel):
    expression: str
    """Expression to evaluate for the replacement value."""


RewriteURIPart: TypeAlias = Union[StaticValue, DynamicValue]
