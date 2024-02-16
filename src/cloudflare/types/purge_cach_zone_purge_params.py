# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "Ikgtf7G3Flex",
    "Ikgtf7G3Everything",
    "Ikgtf7G3Files",
    "Ikgtf7G3FilesFile",
    "Ikgtf7G3FilesFileIkgtf7G3URLAndHeaders",
]


class Ikgtf7G3Flex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class Ikgtf7G3Everything(TypedDict, total=False):
    purge_everything: bool


class Ikgtf7G3Files(TypedDict, total=False):
    files: List[Ikgtf7G3FilesFile]


class Ikgtf7G3FilesFileIkgtf7G3URLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


Ikgtf7G3FilesFile = Union[str, Ikgtf7G3FilesFileIkgtf7G3URLAndHeaders]

PurgeCachZonePurgeParams = Union[Ikgtf7G3Flex, Ikgtf7G3Everything, Ikgtf7G3Files]
