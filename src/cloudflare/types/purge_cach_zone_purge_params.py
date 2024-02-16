# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "JIaMi3xIFlex",
    "JIaMi3xIEverything",
    "JIaMi3xIFiles",
    "JIaMi3xIFilesFile",
    "JIaMi3xIFilesFileJIaMi3xIURLAndHeaders",
]


class JIaMi3xIFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class JIaMi3xIEverything(TypedDict, total=False):
    purge_everything: bool


class JIaMi3xIFiles(TypedDict, total=False):
    files: List[JIaMi3xIFilesFile]


class JIaMi3xIFilesFileJIaMi3xIURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


JIaMi3xIFilesFile = Union[str, JIaMi3xIFilesFileJIaMi3xIURLAndHeaders]

PurgeCachZonePurgeParams = Union[JIaMi3xIFlex, JIaMi3xIEverything, JIaMi3xIFiles]
