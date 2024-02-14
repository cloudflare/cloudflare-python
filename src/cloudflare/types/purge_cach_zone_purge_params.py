# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "OkX7gBs6Flex",
    "OkX7gBs6Everything",
    "OkX7gBs6Files",
    "OkX7gBs6FilesFile",
    "OkX7gBs6FilesFileOkX7gBs6URLAndHeaders",
]


class OkX7gBs6Flex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class OkX7gBs6Everything(TypedDict, total=False):
    purge_everything: bool


class OkX7gBs6Files(TypedDict, total=False):
    files: List[OkX7gBs6FilesFile]


class OkX7gBs6FilesFileOkX7gBs6URLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


OkX7gBs6FilesFile = Union[str, OkX7gBs6FilesFileOkX7gBs6URLAndHeaders]

PurgeCachZonePurgeParams = Union[OkX7gBs6Flex, OkX7gBs6Everything, OkX7gBs6Files]
