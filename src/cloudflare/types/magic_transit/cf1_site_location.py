# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Cf1SiteLocation"]


class Cf1SiteLocation(BaseModel):
    lat: Optional[float] = None
    """Latitude of the CF1 Site."""

    long: Optional[float] = None
    """Longitude of the CF1 Site."""

    name: Optional[str] = None
    """Name of nearest town, city, or village."""
