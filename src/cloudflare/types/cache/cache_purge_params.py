# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = [
    "CachePurgeParams",
    "CachePurgeTags",
    "CachePurgeHosts",
    "CachePurgePrefixes",
    "CachePurgeEverything",
    "CachePurgeFiles",
    "CachePurgeFilesFile",
    "CachePurgeFilesFileCachePurgeURLAndHeaders",
]


class CachePurgeTags(TypedDict, total=False):
    zone_id: Required[str]

    tags: List[str]


class CachePurgeHosts(TypedDict, total=False):
    zone_id: Required[str]

    hosts: List[str]


class CachePurgePrefixes(TypedDict, total=False):
    zone_id: Required[str]

    prefixes: List[str]


class CachePurgeEverything(TypedDict, total=False):
    zone_id: Required[str]

    purge_everything: bool


class CachePurgeFiles(TypedDict, total=False):
    zone_id: Required[str]

    files: List[CachePurgeFilesFile]


class CachePurgeFilesFileCachePurgeURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


CachePurgeFilesFile = Union[str, CachePurgeFilesFileCachePurgeURLAndHeaders]

CachePurgeParams = Union[CachePurgeTags, CachePurgeHosts, CachePurgePrefixes, CachePurgeEverything, CachePurgeFiles]
