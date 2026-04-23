# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["MemberGetResponse", "User"]


class User(BaseModel):
    """Details of the user associated with this membership."""

    id: Optional[str] = None
    """User identifier tag."""

    email: Optional[str] = None
    """The contact email address of the user."""

    first_name: Optional[str] = None
    """User's first name."""

    last_name: Optional[str] = None
    """User's last name."""


class MemberGetResponse(BaseModel):
    """Detailed member information for a User Group member."""

    id: str
    """Account member identifier."""

    created_at: Optional[datetime] = None
    """When the member was added to the user group."""

    email: Optional[str] = None
    """The contact email address of the user."""

    status: Optional[Literal["accepted", "pending"]] = None
    """The member's status in the account."""

    user: Optional[User] = None
    """Details of the user associated with this membership."""
