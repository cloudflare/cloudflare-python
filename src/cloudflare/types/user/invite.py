# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from datetime import datetime

from ..shared.role import Role

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Invite"]

class Invite(BaseModel):
    invited_member_id: Optional[str] = None
    """ID of the user to add to the organization."""

    organization_id: str
    """ID of the organization the user will be added to."""

    id: Optional[str] = None
    """Invite identifier tag."""

    expires_on: Optional[datetime] = None
    """When the invite is no longer active."""

    invited_by: Optional[str] = None
    """The email address of the user who created the invite."""

    invited_member_email: Optional[str] = None
    """Email address of the user to add to the organization."""

    invited_on: Optional[datetime] = None
    """When the invite was sent."""

    organization_name: Optional[str] = None
    """Organization name."""

    roles: Optional[List[Role]] = None
    """Roles to be assigned to this user."""

    status: Optional[Literal["pending", "accepted", "rejected", "expired"]] = None
    """Current status of the invitation."""