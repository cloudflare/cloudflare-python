# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse"]


class URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse(BaseModel):
    scope: Optional[str] = None
    """The scope of the URL normalization."""

    type: Optional[str] = None
    """The type of URL normalization performed by Cloudflare."""
