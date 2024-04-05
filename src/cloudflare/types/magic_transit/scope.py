# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .colo_names_item import ColoNamesItem
from .colo_regions_item import ColoRegionsItem

__all__ = ["Scope"]


class Scope(BaseModel):
    colo_names: Optional[List[ColoNamesItem]] = None
    """List of colo names for the ECMP scope."""

    colo_regions: Optional[List[ColoRegionsItem]] = None
    """List of colo regions for the ECMP scope."""
