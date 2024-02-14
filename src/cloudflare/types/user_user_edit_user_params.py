# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["UserUserEditUserParams"]


class UserUserEditUserParams(TypedDict, total=False):
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
