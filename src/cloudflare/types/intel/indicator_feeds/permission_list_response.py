# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["PermissionListResponse", "PermissionListResponseItem"]


class PermissionListResponseItem(BaseModel):
    id: Optional[int] = None
    """The unique identifier for the indicator feed"""

    description: Optional[str] = None
    """The description of the example test"""

    name: Optional[str] = None
    """The name of the indicator feed"""


PermissionListResponse = List[PermissionListResponseItem]
