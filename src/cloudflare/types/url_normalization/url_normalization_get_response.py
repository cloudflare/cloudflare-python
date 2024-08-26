# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["URLNormalizationGetResponse"]


class URLNormalizationGetResponse(BaseModel):
    scope: Optional[str] = None
    """The scope of the URL normalization."""

    type: Optional[str] = None
    """The type of URL normalization performed by Cloudflare."""
