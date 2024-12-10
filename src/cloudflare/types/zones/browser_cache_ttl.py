# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BrowserCacheTTL"]


class BrowserCacheTTL(BaseModel):
    id: Optional[Literal["browser_cache_ttl"]] = None
    """Control how long resources cached by client browsers remain valid."""

    value: Optional[int] = None
    """The number of seconds to cache resources for.

    The API prohibits setting this to 0 for non-Enterprise domains.
    """
