# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "FJgeoqXqFlex",
    "FJgeoqXqEverything",
    "FJgeoqXqFiles",
    "FJgeoqXqFilesFile",
    "FJgeoqXqFilesFileFJgeoqXqURLAndHeaders",
]


class FJgeoqXqFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class FJgeoqXqEverything(TypedDict, total=False):
    purge_everything: bool


class FJgeoqXqFiles(TypedDict, total=False):
    files: List[FJgeoqXqFilesFile]


class FJgeoqXqFilesFileFJgeoqXqURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


FJgeoqXqFilesFile = Union[str, FJgeoqXqFilesFileFJgeoqXqURLAndHeaders]

PurgeCachZonePurgeParams = Union[FJgeoqXqFlex, FJgeoqXqEverything, FJgeoqXqFiles]
