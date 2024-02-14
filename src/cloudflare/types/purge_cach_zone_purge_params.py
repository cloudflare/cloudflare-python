# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "DRfY4fceFlex",
    "DRfY4fceEverything",
    "DRfY4fceFiles",
    "DRfY4fceFilesFile",
    "DRfY4fceFilesFileDRfY4fceURLAndHeaders",
]


class DRfY4fceFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class DRfY4fceEverything(TypedDict, total=False):
    purge_everything: bool


class DRfY4fceFiles(TypedDict, total=False):
    files: List[DRfY4fceFilesFile]


class DRfY4fceFilesFileDRfY4fceURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


DRfY4fceFilesFile = Union[str, DRfY4fceFilesFileDRfY4fceURLAndHeaders]

PurgeCachZonePurgeParams = Union[DRfY4fceFlex, DRfY4fceEverything, DRfY4fceFiles]
