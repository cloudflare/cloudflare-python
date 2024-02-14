# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "OrganizationUserSOrganizationsListOrganizationsResponse",
    "OrganizationUserSOrganizationsListOrganizationsResponseItem",
]


class OrganizationUserSOrganizationsListOrganizationsResponseItem(BaseModel):
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


OrganizationUserSOrganizationsListOrganizationsResponse = List[
    OrganizationUserSOrganizationsListOrganizationsResponseItem
]
