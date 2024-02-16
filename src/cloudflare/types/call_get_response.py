# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CallGetResponse"]


class CallGetResponse(BaseModel):
    created: Optional[datetime] = None
    """The date and time the item was created."""

    modified: Optional[datetime] = None
    """The date and time the item was last modified."""

    name: Optional[str] = None
    """A short description of Calls app, not shown to end users."""

    uid: Optional[str] = None
    """A Cloudflare-generated unique identifier for a item."""
