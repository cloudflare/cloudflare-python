# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "MsVw2EBcFlex",
    "MsVw2EBcEverything",
    "MsVw2EBcFiles",
    "MsVw2EBcFilesFile",
    "MsVw2EBcFilesFileMsVw2EBcURLAndHeaders",
]


class MsVw2EBcFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class MsVw2EBcEverything(TypedDict, total=False):
    purge_everything: bool


class MsVw2EBcFiles(TypedDict, total=False):
    files: List[MsVw2EBcFilesFile]


class MsVw2EBcFilesFileMsVw2EBcURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


MsVw2EBcFilesFile = Union[str, MsVw2EBcFilesFileMsVw2EBcURLAndHeaders]

PurgeCachZonePurgeParams = Union[MsVw2EBcFlex, MsVw2EBcEverything, MsVw2EBcFiles]
