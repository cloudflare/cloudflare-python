# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "NuRynDznFlex",
    "NuRynDznEverything",
    "NuRynDznFiles",
    "NuRynDznFilesFile",
    "NuRynDznFilesFileNuRynDznURLAndHeaders",
]


class NuRynDznFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class NuRynDznEverything(TypedDict, total=False):
    purge_everything: bool


class NuRynDznFiles(TypedDict, total=False):
    files: List[NuRynDznFilesFile]


class NuRynDznFilesFileNuRynDznURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


NuRynDznFilesFile = Union[str, NuRynDznFilesFileNuRynDznURLAndHeaders]

PurgeCachZonePurgeParams = Union[NuRynDznFlex, NuRynDznEverything, NuRynDznFiles]
