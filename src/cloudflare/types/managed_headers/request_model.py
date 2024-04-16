# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RequestModel"]


class RequestModel(BaseModel):
    id: Optional[str] = None
    """Human-readable identifier of the Managed Transform."""

    enabled: Optional[bool] = None
    """When true, the Managed Transform is enabled."""
