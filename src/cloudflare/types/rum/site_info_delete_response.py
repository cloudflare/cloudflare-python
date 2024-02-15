# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SiteInfoDeleteResponse"]


class SiteInfoDeleteResponse(BaseModel):
    site_tag: Optional[str] = None
    """The Web Analytics site identifier."""
