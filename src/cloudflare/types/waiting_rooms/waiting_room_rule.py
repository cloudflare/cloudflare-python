# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WaitingRoomRule"]


class WaitingRoomRule(BaseModel):
    id: Optional[str] = None
    """The ID of the rule."""

    action: Optional[Literal["bypass_waiting_room"]] = None
    """The action to take when the expression matches."""

    description: Optional[str] = None
    """The description of the rule."""

    enabled: Optional[bool] = None
    """When set to true, the rule is enabled."""

    expression: Optional[str] = None
    """Criteria defining when there is a match for the current rule."""

    last_updated: Optional[datetime] = None

    version: Optional[str] = None
    """The version of the rule."""
