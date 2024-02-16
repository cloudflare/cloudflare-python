# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "XOjsLkXnFlex",
    "XOjsLkXnEverything",
    "XOjsLkXnFiles",
    "XOjsLkXnFilesFile",
    "XOjsLkXnFilesFileXOjsLkXnURLAndHeaders",
]


class XOjsLkXnFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class XOjsLkXnEverything(TypedDict, total=False):
    purge_everything: bool


class XOjsLkXnFiles(TypedDict, total=False):
    files: List[XOjsLkXnFilesFile]


class XOjsLkXnFilesFileXOjsLkXnURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


XOjsLkXnFilesFile = Union[str, XOjsLkXnFilesFileXOjsLkXnURLAndHeaders]

PurgeCachZonePurgeParams = Union[XOjsLkXnFlex, XOjsLkXnEverything, XOjsLkXnFiles]
