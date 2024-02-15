# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "N2QfWbz7Flex",
    "N2QfWbz7Everything",
    "N2QfWbz7Files",
    "N2QfWbz7FilesFile",
    "N2QfWbz7FilesFileN2QfWbz7URLAndHeaders",
]


class N2QfWbz7Flex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class N2QfWbz7Everything(TypedDict, total=False):
    purge_everything: bool


class N2QfWbz7Files(TypedDict, total=False):
    files: List[N2QfWbz7FilesFile]


class N2QfWbz7FilesFileN2QfWbz7URLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


N2QfWbz7FilesFile = Union[str, N2QfWbz7FilesFileN2QfWbz7URLAndHeaders]

PurgeCachZonePurgeParams = Union[N2QfWbz7Flex, N2QfWbz7Everything, N2QfWbz7Files]
