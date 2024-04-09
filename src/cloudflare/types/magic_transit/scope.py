# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .colo_name import ColoName
from .colo_region import ColoRegion

__all__ = ["Scope"]


class Scope(BaseModel):
    colo_names: Optional[List[ColoName]] = None
    """List of colo names for the ECMP scope."""

    colo_regions: Optional[List[ColoRegion]] = None
    """List of colo regions for the ECMP scope."""
