# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .site import Site
from ..._models import BaseModel

__all__ = ["SiteGetResponse"]


class SiteGetResponse(BaseModel):
    site: Optional[Site] = None
