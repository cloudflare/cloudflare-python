# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BrowserCacheTTLParam"]


class BrowserCacheTTLParam(TypedDict, total=False):
    id: Literal["browser_cache_ttl"]
    """Control how long resources cached by client browsers remain valid."""

    value: int
    """The number of seconds to cache resources for. Minimum values by plan:

    - Free: 7200 seconds (2 hours)
    - Pro: 3600 seconds (1 hour)
    - Business: 1 second
    - Enterprise: 1 second Setting this to 0 enables "Respect Existing Headers" and
      is allowed for all plans.
    """
