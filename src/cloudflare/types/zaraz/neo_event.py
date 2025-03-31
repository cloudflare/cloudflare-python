# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NeoEvent"]


class NeoEvent(BaseModel):
    action_type: str = FieldInfo(alias="actionType")
    """Tool event type"""

    blocking_triggers: List[str] = FieldInfo(alias="blockingTriggers")
    """List of blocking triggers IDs"""

    data: object
    """Event payload"""

    firing_triggers: List[str] = FieldInfo(alias="firingTriggers")
    """List of firing triggers IDs"""
