# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .site import Site
from ..._models import BaseModel

__all__ = ["SiteUpdateResponse"]


class SiteUpdateResponse(BaseModel):
    site: Optional[Site] = None
