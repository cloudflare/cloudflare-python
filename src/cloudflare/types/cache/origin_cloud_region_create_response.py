# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .origin_cloud_region import OriginCloudRegion

__all__ = ["OriginCloudRegionCreateResponse"]


class OriginCloudRegionCreateResponse(BaseModel):
    """Response result for a single origin cloud region mapping."""

    id: Literal["origin_public_cloud_region"]

    editable: bool
    """Whether the setting can be modified by the current user."""

    value: OriginCloudRegion
    """A single origin IP-to-cloud-region mapping."""

    modified_on: Optional[datetime] = None
    """Time the mapping was last modified."""
