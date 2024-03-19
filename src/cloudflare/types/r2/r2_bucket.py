# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["R2Bucket"]


class R2Bucket(BaseModel):
    creation_date: Optional[str] = None
    """Creation timestamp"""

    location: Optional[Literal["apac", "eeur", "enam", "weur", "wnam"]] = None
    """Location of the bucket"""

    name: Optional[str] = None
    """Name of the bucket"""
