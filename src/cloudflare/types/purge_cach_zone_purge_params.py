# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "MYgWnpy2Flex",
    "MYgWnpy2Everything",
    "MYgWnpy2Files",
    "MYgWnpy2FilesFile",
    "MYgWnpy2FilesFileMYgWnpy2URLAndHeaders",
]


class MYgWnpy2Flex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class MYgWnpy2Everything(TypedDict, total=False):
    purge_everything: bool


class MYgWnpy2Files(TypedDict, total=False):
    files: List[MYgWnpy2FilesFile]


class MYgWnpy2FilesFileMYgWnpy2URLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


MYgWnpy2FilesFile = Union[str, MYgWnpy2FilesFileMYgWnpy2URLAndHeaders]

PurgeCachZonePurgeParams = Union[MYgWnpy2Flex, MYgWnpy2Everything, MYgWnpy2Files]
