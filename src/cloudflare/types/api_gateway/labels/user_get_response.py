# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["UserGetResponse"]


class UserGetResponse(BaseModel):
    created_at: datetime

    description: str
    """The description of the label"""

    last_updated: datetime

    metadata: object
    """Metadata for the label"""

    name: str
    """The name of the label"""

    source: Literal["user", "managed"]
    """
    - `user` - label is owned by the user
    - `managed` - label is owned by cloudflare
    """

    mapped_resources: Optional[object] = None
    """Provides counts of what resources are linked to this label"""
