# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AutomaticHTTPSRewrites"]


class AutomaticHTTPSRewrites(BaseModel):
    id: Optional[Literal["automatic_https_rewrites"]] = None
    """Turn on or off Automatic HTTPS Rewrites."""

    value: Optional[Literal["on", "off"]] = None
    """The status of Automatic HTTPS Rewrites."""
