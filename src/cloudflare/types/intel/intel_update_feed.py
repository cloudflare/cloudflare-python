# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IntelUpdateFeed"]


class IntelUpdateFeed(BaseModel):
    file_id: Optional[int] = None
    """Feed id"""

    filename: Optional[str] = None
    """Name of the file unified in our system"""

    status: Optional[str] = None
    """Current status of upload, should be unified"""
