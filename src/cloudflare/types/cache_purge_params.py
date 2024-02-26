# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = [
    "CachePurgeParams",
    "Body",
    "BodyCachePurgeFlex",
    "BodyCachePurgeFlexCachePurgeTags",
    "BodyCachePurgeFlexCachePurgeHosts",
    "BodyCachePurgeFlexCachePurgePrefixes",
    "BodyCachePurgeEverything",
    "BodyCachePurgeFiles",
    "BodyCachePurgeFilesFile",
    "BodyCachePurgeFilesFileCachePurgeURLAndHeaders",
]


class CachePurgeParams(TypedDict, total=False):
    body: Required[Body]


class BodyCachePurgeFlexCachePurgeTags(TypedDict, total=False):
    tags: List[str]


class BodyCachePurgeFlexCachePurgeHosts(TypedDict, total=False):
    hosts: List[str]


class BodyCachePurgeFlexCachePurgePrefixes(TypedDict, total=False):
    prefixes: List[str]


BodyCachePurgeFlex = Union[
    BodyCachePurgeFlexCachePurgeTags, BodyCachePurgeFlexCachePurgeHosts, BodyCachePurgeFlexCachePurgePrefixes
]


class BodyCachePurgeEverything(TypedDict, total=False):
    purge_everything: bool


class BodyCachePurgeFilesFileCachePurgeURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


BodyCachePurgeFilesFile = Union[str, BodyCachePurgeFilesFileCachePurgeURLAndHeaders]


class BodyCachePurgeFiles(TypedDict, total=False):
    files: List[BodyCachePurgeFilesFile]


Body = Union[BodyCachePurgeFlex, BodyCachePurgeEverything, BodyCachePurgeFiles]
