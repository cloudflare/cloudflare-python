# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .organization import Organization

__all__ = ["UserEditResponse"]


class UserEditResponse(BaseModel):
    id: Optional[str] = None
    """Identifier of the user."""

    betas: Optional[List[str]] = None
    """Lists the betas that the user is participating in."""

    country: Optional[str] = None
    """The country in which the user lives."""

    first_name: Optional[str] = None
    """User's first name"""

    has_business_zones: Optional[bool] = None
    """Indicates whether user has any business zones"""

    has_enterprise_zones: Optional[bool] = None
    """Indicates whether user has any enterprise zones"""

    has_pro_zones: Optional[bool] = None
    """Indicates whether user has any pro zones"""

    last_name: Optional[str] = None
    """User's last name"""

    organizations: Optional[List[Organization]] = None

    suspended: Optional[bool] = None
    """Indicates whether user has been suspended"""

    telephone: Optional[str] = None
    """User's telephone number"""

    two_factor_authentication_enabled: Optional[bool] = None
    """Indicates whether two-factor authentication is enabled for the user account.

    Does not apply to API authentication.
    """

    two_factor_authentication_locked: Optional[bool] = None
    """
    Indicates whether two-factor authentication is required by one of the accounts
    that the user is a member of.
    """

    zipcode: Optional[str] = None
    """The zipcode or postal code where the user lives."""
