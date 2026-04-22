# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .origin_cloud_region import OriginCloudRegion

__all__ = ["OriginCloudRegionEditResponse"]


class OriginCloudRegionEditResponse(BaseModel):
    """Response result for a list of origin cloud region mappings."""

    id: Literal["origin_public_cloud_region"]

    editable: bool
    """Whether the setting can be modified by the current user."""

    value: List[OriginCloudRegion]

    modified_on: Optional[datetime] = None
    """Time the mapping set was last modified. Null when no mappings exist."""
