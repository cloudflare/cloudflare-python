# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .site import Site
from ..._models import BaseModel

__all__ = ["SiteListResponse"]


class SiteListResponse(BaseModel):
    sites: Optional[List[Site]] = None
