# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ......_models import BaseModel

__all__ = ["UserListResponse", "UserListResponseItem"]


class UserListResponseItem(BaseModel):
    id: Optional[str] = None
    """UUID"""

    email: Optional[str] = None
    """The email of the user."""

    name: Optional[str] = None
    """The name of the user."""

    status: Optional[Literal["approved", "blocked"]] = None
    """Policy evaluation result for an individual user."""


UserListResponse: TypeAlias = List[UserListResponseItem]
