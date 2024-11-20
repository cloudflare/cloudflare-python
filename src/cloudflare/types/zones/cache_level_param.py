# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CacheLevelParam"]


class CacheLevelParam(TypedDict, total=False):
    id: Literal["cache_level"]
    """Apply custom caching based on the option selected."""

    value: Literal["bypass", "basic", "simplified", "aggressive", "cache_everything"]
    """
    - `bypass`: Cloudflare does not cache.
    - `basic`: Delivers resources from cache when there is no query string.
    - `simplified`: Delivers the same resource to everyone independent of the query
      string.
    - `aggressive`: Caches all static content that has a query string.
    - `cache_everything`: Treats all content as static and caches all file types
      beyond the
      [Cloudflare default cached content](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/#default-cached-file-extensions).
    """
