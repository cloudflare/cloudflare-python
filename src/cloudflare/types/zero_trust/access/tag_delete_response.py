# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TagDeleteResponse"]


class TagDeleteResponse(BaseModel):
    name: Optional[str] = None
    """The name of the tag"""
