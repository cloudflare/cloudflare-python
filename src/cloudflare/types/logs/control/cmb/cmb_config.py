# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["CmbConfig"]


class CmbConfig(BaseModel):
    allow_out_of_region_access: Optional[bool] = None
    """Allow out of region access"""

    regions: Optional[str] = None
    """Name of the region."""
