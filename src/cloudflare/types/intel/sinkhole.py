# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Sinkhole"]


class Sinkhole(BaseModel):
    id: Optional[int] = None
    """The unique identifier for the sinkhole"""

    account_tag: Optional[str] = None
    """The account tag that owns this sinkhole"""

    created_on: Optional[datetime] = None
    """The date and time when the sinkhole was created"""

    modified_on: Optional[datetime] = None
    """The date and time when the sinkhole was last modified"""

    name: Optional[str] = None
    """The name of the sinkhole"""

    r2_bucket: Optional[str] = None
    """The name of the R2 bucket to store results"""

    r2_id: Optional[str] = None
    """The id of the R2 instance"""
