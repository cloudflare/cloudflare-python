# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .iam_schemas_role import IamSchemasRole

__all__ = ["MemberListResponse"]


class MemberListResponse(BaseModel):
    id: str
    """Identifier"""

    email: str
    """The contact email address of the user."""

    name: Optional[str] = None
    """Member Name."""

    roles: List[IamSchemasRole]
    """Roles assigned to this Member."""

    status: Literal["accepted", "invited"]
    """A member's status in the organization."""
