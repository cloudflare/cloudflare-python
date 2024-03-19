# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IamOrganization"]


class IamOrganization(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """Organization name."""

    permissions: Optional[List[str]] = None
    """Access permissions for this User."""

    roles: Optional[List[str]] = None
    """List of roles that a user has within an organization."""

    status: Optional[Literal["member", "invited"]] = None
    """Whether the user is a member of the organization or has an inivitation pending."""
