# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["MemberCreateResponse"]


class MemberCreateResponse(BaseModel):
    id: str
    """Account member identifier."""

    email: Optional[str] = None
    """The contact email address of the user."""

    status: Optional[Literal["accepted", "pending"]] = None
    """The member's status in the account."""
