# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .cf1_site_location import Cf1SiteLocation

__all__ = ["Cf1Site"]


class Cf1Site(BaseModel):
    name: str
    """
    A human-provided name describing the CF1 Site that should be unique within the
    account.
    """

    id: Optional[str] = None
    """Identifier"""

    created_on: Optional[datetime] = None

    description: Optional[str] = None
    """A human-provided description of the CF1 Site."""

    location: Optional[Cf1SiteLocation] = None

    modified_on: Optional[datetime] = None
