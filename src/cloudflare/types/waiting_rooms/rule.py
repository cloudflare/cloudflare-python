# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Rule"]


class Rule(BaseModel):
    action: Literal["bypass_waiting_room"]
    """The action to take when the expression matches."""

    expression: str
    """Criteria defining when there is a match for the current rule."""

    description: Optional[str] = None
    """The description of the rule."""

    enabled: Optional[bool] = None
    """When set to true, the rule is enabled."""
