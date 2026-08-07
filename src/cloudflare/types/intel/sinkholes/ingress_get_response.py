# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["IngressGetResponse"]


class IngressGetResponse(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the ingress rule."""

    cidr: Optional[str] = None
    """The CIDR block for the ingress rule."""

    created_on: Optional[datetime] = None
    """The date and time when the ingress rule was created."""

    modified_on: Optional[datetime] = None
    """The date and time when the ingress rule was last modified."""

    sinkhole_id: Optional[str] = None
    """The sinkhole this ingress rule belongs to."""

    zone_tag: Optional[str] = None
    """The zone tag associated with this ingress rule."""
