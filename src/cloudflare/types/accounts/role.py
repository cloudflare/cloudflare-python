# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel
from .member_permission import MemberPermission

__all__ = ["Role"]


class Role(BaseModel):
    id: str
    """Role identifier tag."""

    description: str
    """Description of role's permissions."""

    name: str
    """Role name."""

    permissions: MemberPermission
