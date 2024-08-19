# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    id: Optional[str] = None
    """Destination address identifier."""

    created: Optional[datetime] = None
    """The date and time the destination address has been created."""

    email: Optional[str] = None
    """The contact email address of the user."""

    modified: Optional[datetime] = None
    """The date and time the destination address was last modified."""

    tag: Optional[str] = None
    """Destination address tag.

    (Deprecated, replaced by destination address identifier)
    """

    verified: Optional[datetime] = None
    """The date and time the destination address has been verified.

    Null means not verified yet.
    """
