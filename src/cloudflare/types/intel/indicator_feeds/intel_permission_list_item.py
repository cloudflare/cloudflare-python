# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["IntelPermissionListItem"]


class IntelPermissionListItem(BaseModel):
    id: Optional[int] = None
    """The unique identifier for the indicator feed"""

    description: Optional[str] = None
    """The description of the example test"""

    name: Optional[str] = None
    """The name of the indicator feed"""
