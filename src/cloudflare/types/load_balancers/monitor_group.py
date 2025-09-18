# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["MonitorGroup", "Member"]


class Member(BaseModel):
    enabled: bool
    """Whether this monitor is enabled in the group"""

    monitor_id: str
    """
    The ID of the Monitor to use for checking the health of origins within this
    pool.
    """

    monitoring_only: bool
    """Whether this monitor is used for monitoring only (does not affect pool health)"""

    must_be_healthy: bool
    """Whether this monitor must be healthy for the pool to be considered healthy"""

    created_at: Optional[datetime] = None
    """The timestamp of when the monitor was added to the group"""

    updated_at: Optional[datetime] = None
    """The timestamp of when the monitor group member was last updated"""


class MonitorGroup(BaseModel):
    id: str
    """
    The ID of the Monitor Group to use for checking the health of origins within
    this pool.
    """

    description: str
    """A short description of the monitor group"""

    members: List[Member]
    """List of monitors in this group"""

    created_at: Optional[datetime] = None
    """The timestamp of when the monitor group was created"""

    updated_at: Optional[datetime] = None
    """The timestamp of when the monitor group was last updated"""
