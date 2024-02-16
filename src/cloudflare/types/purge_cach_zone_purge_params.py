# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "CkpEqDfYFlex",
    "CkpEqDfYEverything",
    "CkpEqDfYFiles",
    "CkpEqDfYFilesFile",
    "CkpEqDfYFilesFileCkpEqDfYURLAndHeaders",
]


class CkpEqDfYFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class CkpEqDfYEverything(TypedDict, total=False):
    purge_everything: bool


class CkpEqDfYFiles(TypedDict, total=False):
    files: List[CkpEqDfYFilesFile]


class CkpEqDfYFilesFileCkpEqDfYURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


CkpEqDfYFilesFile = Union[str, CkpEqDfYFilesFileCkpEqDfYURLAndHeaders]

PurgeCachZonePurgeParams = Union[CkpEqDfYFlex, CkpEqDfYEverything, CkpEqDfYFiles]
