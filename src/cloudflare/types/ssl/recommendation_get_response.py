# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RecommendationGetResponse"]


class RecommendationGetResponse(BaseModel):
    id: str

    editable: bool
    """Whether this setting can be updated or not."""

    modified_on: datetime
    """Last time this setting was modified."""

    value: Literal["auto", "custom"]
    """Current setting of the automatic SSL/TLS."""

    next_scheduled_scan: Optional[datetime] = None
    """Next time this zone will be scanned by the Automatic SSL/TLS."""
