# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "AQxohOucFlex",
    "AQxohOucEverything",
    "AQxohOucFiles",
    "AQxohOucFilesFile",
    "AQxohOucFilesFileAQxohOucURLAndHeaders",
]


class AQxohOucFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class AQxohOucEverything(TypedDict, total=False):
    purge_everything: bool


class AQxohOucFiles(TypedDict, total=False):
    files: List[AQxohOucFilesFile]


class AQxohOucFilesFileAQxohOucURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


AQxohOucFilesFile = Union[str, AQxohOucFilesFileAQxohOucURLAndHeaders]

PurgeCachZonePurgeParams = Union[AQxohOucFlex, AQxohOucEverything, AQxohOucFiles]
