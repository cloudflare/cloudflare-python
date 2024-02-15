# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "CdqYApz8Flex",
    "CdqYApz8Everything",
    "CdqYApz8Files",
    "CdqYApz8FilesFile",
    "CdqYApz8FilesFileCdqYApz8URLAndHeaders",
]


class CdqYApz8Flex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class CdqYApz8Everything(TypedDict, total=False):
    purge_everything: bool


class CdqYApz8Files(TypedDict, total=False):
    files: List[CdqYApz8FilesFile]


class CdqYApz8FilesFileCdqYApz8URLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


CdqYApz8FilesFile = Union[str, CdqYApz8FilesFileCdqYApz8URLAndHeaders]

PurgeCachZonePurgeParams = Union[CdqYApz8Flex, CdqYApz8Everything, CdqYApz8Files]
