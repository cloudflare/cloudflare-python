# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = ["CachePurgeParams", "File", "FileCachePurgeURLAndHeaders"]


class CachePurgeParams(TypedDict, total=False):
    zone_id: Required[str]

    files: List[File]

    hosts: List[str]

    prefixes: List[str]

    purge_everything: bool

    tags: List[str]


class FileCachePurgeURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


File = Union[str, FileCachePurgeURLAndHeaders]
