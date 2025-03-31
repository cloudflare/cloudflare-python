# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NeoEventParam"]


class NeoEventParam(TypedDict, total=False):
    action_type: Required[Annotated[str, PropertyInfo(alias="actionType")]]
    """Tool event type"""

    blocking_triggers: Required[Annotated[List[str], PropertyInfo(alias="blockingTriggers")]]
    """List of blocking triggers IDs"""

    data: Required[object]
    """Event payload"""

    firing_triggers: Required[Annotated[List[str], PropertyInfo(alias="firingTriggers")]]
    """List of firing triggers IDs"""
