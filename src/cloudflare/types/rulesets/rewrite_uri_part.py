# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["RewriteURIPart", "StaticValue", "DynamicValue"]


class StaticValue(BaseModel):
    value: str
    """Predefined replacement value."""


class DynamicValue(BaseModel):
    expression: str
    """Expression to evaluate for the replacement value."""


RewriteURIPart: TypeAlias = Union[StaticValue, DynamicValue]
