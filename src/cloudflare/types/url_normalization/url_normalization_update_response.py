# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["URLNormalizationUpdateResponse"]


class URLNormalizationUpdateResponse(BaseModel):
    scope: Literal["incoming", "both"]
    """The scope of the URL normalization."""

    type: Literal["cloudflare", "rfc3986"]
    """The type of URL normalization performed by Cloudflare."""
