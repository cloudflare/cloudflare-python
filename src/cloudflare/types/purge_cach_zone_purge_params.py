# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "QBpKLyWfFlex",
    "QBpKLyWfEverything",
    "QBpKLyWfFiles",
    "QBpKLyWfFilesFile",
    "QBpKLyWfFilesFileQBpKLyWfURLAndHeaders",
]


class QBpKLyWfFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class QBpKLyWfEverything(TypedDict, total=False):
    purge_everything: bool


class QBpKLyWfFiles(TypedDict, total=False):
    files: List[QBpKLyWfFilesFile]


class QBpKLyWfFilesFileQBpKLyWfURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


QBpKLyWfFilesFile = Union[str, QBpKLyWfFilesFileQBpKLyWfURLAndHeaders]

PurgeCachZonePurgeParams = Union[QBpKLyWfFlex, QBpKLyWfEverything, QBpKLyWfFiles]
