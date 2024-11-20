# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BrowserCacheTTLParam"]


class BrowserCacheTTLParam(TypedDict, total=False):
    id: Literal["browser_cache_ttl"]
    """Control how long resources cached by client browsers remain valid."""

    value: int
    """The number of seconds to cache resources for.

    The API prohibits setting this to 0 for non-Enterprise domains.
    """
