# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    address: str
    """Address."""

    city: str
    """City."""

    country: Optional[str] = None
    """The country in which the user lives."""

    first_name: Optional[str] = None
    """User's first name"""

    last_name: Optional[str] = None
    """User's last name"""

    organization: str
    """Name of organization."""

    phone: Optional[str] = None
    """User's telephone number"""

    state: str
    """State."""

    zip: Optional[str] = None
    """The zipcode or postal code where the user lives."""

    id: Optional[str] = None
    """Contact Identifier."""

    address2: Optional[str] = None
    """Optional address line for unit, floor, suite, etc."""

    email: Optional[str] = None
    """The contact email address of the user."""

    fax: Optional[str] = None
    """Contact fax number."""
