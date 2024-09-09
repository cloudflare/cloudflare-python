# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FilterOptions"]


class FilterOptions(BaseModel):
    disable: Optional[bool] = None
    """If set true, disable notifications for this type of resource (pool or origin)."""

    healthy: Optional[bool] = None
    """If present, send notifications only for this health status (e.g.

    false for only DOWN events). Use null to reset (all events).
    """
