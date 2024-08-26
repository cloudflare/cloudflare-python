# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserEditParams"]


class UserEditParams(TypedDict, total=False):
    country: Optional[str]
    """The country in which the user lives."""

    first_name: Optional[str]
    """User's first name"""

    last_name: Optional[str]
    """User's last name"""

    telephone: Optional[str]
    """User's telephone number"""

    zipcode: Optional[str]
    """The zipcode or postal code where the user lives."""
