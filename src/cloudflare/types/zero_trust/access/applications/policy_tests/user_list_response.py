# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ......_models import BaseModel

from typing import Optional

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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
