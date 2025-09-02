# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "CachePurgeParams",
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
    """
    For more information on cache tags and purging by tags, please refer to
    [purge by cache-tags documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/).
    """


class CachePurgeFlexPurgeByHostnames(TypedDict, total=False):
    zone_id: Required[str]

    hosts: SequenceNotStr[str]
    """
    For more information purging by hostnames, please refer to
    [purge by hostname documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/).
    """


class CachePurgeFlexPurgeByPrefixes(TypedDict, total=False):
    zone_id: Required[str]

    prefixes: SequenceNotStr[str]
    """
    For more information on purging by prefixes, please refer to
    [purge by prefix documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/).
    """


class CachePurgeEverything(TypedDict, total=False):
    zone_id: Required[str]

    purge_everything: bool
    """
    For more information, please refer to
    [purge everything documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/).
    """


class CachePurgeSingleFile(TypedDict, total=False):
    zone_id: Required[str]

    files: SequenceNotStr[str]
    """
    For more information on purging files, please refer to
    [purge by single-file documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).
    """


class CachePurgeSingleFileWithURLAndHeaders(TypedDict, total=False):
    zone_id: Required[str]

    files: Iterable[CachePurgeSingleFileWithURLAndHeadersFile]
    """
    For more information on purging files with URL and headers, please refer to
    [purge by single-file documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/).
    """


class CachePurgeSingleFileWithURLAndHeadersFile(TypedDict, total=False):
    headers: Dict[str, str]

    url: str


CachePurgeParams: TypeAlias = Union[
    CachePurgeFlexPurgeByTags,
    CachePurgeFlexPurgeByHostnames,
    CachePurgeFlexPurgeByPrefixes,
    CachePurgeEverything,
    CachePurgeSingleFile,
    CachePurgeSingleFileWithURLAndHeaders,
]
