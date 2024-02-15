# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "Rpj5a2L2Flex",
    "Rpj5a2L2Everything",
    "Rpj5a2L2Files",
    "Rpj5a2L2FilesFile",
    "Rpj5a2L2FilesFileRpj5a2L2URLAndHeaders",
]


class Rpj5a2L2Flex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class Rpj5a2L2Everything(TypedDict, total=False):
    purge_everything: bool


class Rpj5a2L2Files(TypedDict, total=False):
    files: List[Rpj5a2L2FilesFile]


class Rpj5a2L2FilesFileRpj5a2L2URLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


Rpj5a2L2FilesFile = Union[str, Rpj5a2L2FilesFileRpj5a2L2URLAndHeaders]

PurgeCachZonePurgeParams = Union[Rpj5a2L2Flex, Rpj5a2L2Everything, Rpj5a2L2Files]
