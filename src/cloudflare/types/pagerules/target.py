# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Target", "Constraint"]


class Constraint(BaseModel):
    operator: Literal["matches", "contains", "equals", "not_equal", "not_contain"]
    """
    The matches operator can use asterisks and pipes as wildcard and 'or' operators.
    """

    value: str
    """The URL pattern to match against the current request.

    The pattern may contain up to four asterisks ('\\**') as placeholders.
    """


class Target(BaseModel):
    constraint: Optional[Constraint] = None
    """String constraint."""

    target: Optional[Literal["url"]] = None
    """A target based on the URL of the request."""
