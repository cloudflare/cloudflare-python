# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .filter_options import FilterOptions

__all__ = ["NotificationFilter"]


class NotificationFilter(BaseModel):
    origin: Optional[FilterOptions] = None
    """Filter options for a particular resource type (pool or origin).

    Use null to reset.
    """

    pool: Optional[FilterOptions] = None
    """Filter options for a particular resource type (pool or origin).

    Use null to reset.
    """
