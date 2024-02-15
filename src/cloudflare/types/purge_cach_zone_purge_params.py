# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "QxCcLmCpFlex",
    "QxCcLmCpEverything",
    "QxCcLmCpFiles",
    "QxCcLmCpFilesFile",
    "QxCcLmCpFilesFileQxCcLmCpURLAndHeaders",
]


class QxCcLmCpFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class QxCcLmCpEverything(TypedDict, total=False):
    purge_everything: bool


class QxCcLmCpFiles(TypedDict, total=False):
    files: List[QxCcLmCpFilesFile]


class QxCcLmCpFilesFileQxCcLmCpURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


QxCcLmCpFilesFile = Union[str, QxCcLmCpFilesFileQxCcLmCpURLAndHeaders]

PurgeCachZonePurgeParams = Union[QxCcLmCpFlex, QxCcLmCpEverything, QxCcLmCpFiles]
