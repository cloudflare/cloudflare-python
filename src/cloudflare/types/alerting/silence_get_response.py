# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SilenceGetResponse"]


class SilenceGetResponse(BaseModel):
    id: Optional[str] = None
    """Silence ID"""

    created_at: Optional[str] = None
    """When the silence was created."""

    end_time: Optional[str] = None
    """When the silence ends."""

    policy_id: Optional[str] = None
    """The unique identifier of a notification policy"""

    start_time: Optional[str] = None
    """When the silence starts."""

    updated_at: Optional[str] = None
    """When the silence was modified."""
