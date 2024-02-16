# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "K9HAoHwQFlex",
    "K9HAoHwQEverything",
    "K9HAoHwQFiles",
    "K9HAoHwQFilesFile",
    "K9HAoHwQFilesFileK9HAoHwQURLAndHeaders",
]


class K9HAoHwQFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class K9HAoHwQEverything(TypedDict, total=False):
    purge_everything: bool


class K9HAoHwQFiles(TypedDict, total=False):
    files: List[K9HAoHwQFilesFile]


class K9HAoHwQFilesFileK9HAoHwQURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


K9HAoHwQFilesFile = Union[str, K9HAoHwQFilesFileK9HAoHwQURLAndHeaders]

PurgeCachZonePurgeParams = Union[K9HAoHwQFlex, K9HAoHwQEverything, K9HAoHwQFiles]
