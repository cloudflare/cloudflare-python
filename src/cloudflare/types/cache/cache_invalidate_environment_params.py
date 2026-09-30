# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "CacheInvalidateEnvironmentParams",
    "CachePurgeFlexPurgeByTags",
    "CachePurgeFlexPurgeByHostnames",
    "CachePurgeFlexPurgeByPrefixes",
    "CachePurgeEverything",
    "CachePurgeSingleFile",
    "CachePurgeSingleFileWithURLAndHeaders",
    "CachePurgeSingleFileWithURLAndHeadersFile",
]


class CachePurgeFlexPurgeByTags(TypedDict, total=False):
    zone_id: Required[str]

    tags: SequenceNotStr[str]
    """Cache tags.

    Targets all content whose `Cache-Tag` response header contains at least one of
    these tags. See
    [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).
    """


class CachePurgeFlexPurgeByHostnames(TypedDict, total=False):
    zone_id: Required[str]

    hosts: SequenceNotStr[str]
    """Hostnames, such as `www.example.com`.

    Targets all content cached for these hostnames. See
    [Purge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).
    """


class CachePurgeFlexPurgeByPrefixes(TypedDict, total=False):
    zone_id: Required[str]

    prefixes: SequenceNotStr[str]
    """
    URL prefixes, each a hostname followed by a path, such as
    `www.example.com/blog/`. Targets all content whose URL starts with one of these
    prefixes. Do not include a scheme, query string, or fragment. See
    [Purge cache by prefix](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).
    """


class CachePurgeEverything(TypedDict, total=False):
    zone_id: Required[str]

    purge_everything: bool
    """
    Set to `true` to target all cached content in the zone, or in the environment
    for the environment endpoints. Must be the only field in the request. See
    [Purge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).
    """


class CachePurgeSingleFile(TypedDict, total=False):
    zone_id: Required[str]

    files: SequenceNotStr[str]
    """Full URLs, such as `https://www.example.com/css/styles.css`.

    Targets the content cached for each URL. If your cache key includes request
    headers, send objects with `url` and `headers` instead. See
    [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).
    """


class CachePurgeSingleFileWithURLAndHeaders(TypedDict, total=False):
    zone_id: Required[str]

    files: Iterable[CachePurgeSingleFileWithURLAndHeadersFile]
    """URLs with the request headers your cache key uses.

    Use this form when your cache key includes request headers, or the visitor's
    device type, country, or language: send the header values each URL was cached
    with, such as `CF-Device-Type`, `CF-IPCountry`, or `Accept-Language`.

    When you send the `Origin` header, include the scheme and hostname. Include the
    port unless it is the default for the scheme: 80 for `http`, 443 for `https`.

    See
    [Purge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).
    """


class CachePurgeSingleFileWithURLAndHeadersFile(TypedDict, total=False):
    headers: Dict[str, str]
    """Request headers and the values the content was cached with."""

    url: str
    """Full URL of the content."""


CacheInvalidateEnvironmentParams: TypeAlias = Union[
    CachePurgeFlexPurgeByTags,
    CachePurgeFlexPurgeByHostnames,
    CachePurgeFlexPurgeByPrefixes,
    CachePurgeEverything,
    CachePurgeSingleFile,
    CachePurgeSingleFileWithURLAndHeaders,
]
