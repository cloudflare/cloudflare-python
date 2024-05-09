# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Scope"]


class Scope(BaseModel):
    colo_names: Optional[List[str]] = None
    """List of colo names for the ECMP scope."""

    colo_regions: Optional[List[str]] = None
    """List of colo regions for the ECMP scope."""
