# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "E1GoErmIFlex",
    "E1GoErmIEverything",
    "E1GoErmIFiles",
    "E1GoErmIFilesFile",
    "E1GoErmIFilesFileE1GoErmIURLAndHeaders",
]


class E1GoErmIFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class E1GoErmIEverything(TypedDict, total=False):
    purge_everything: bool


class E1GoErmIFiles(TypedDict, total=False):
    files: List[E1GoErmIFilesFile]


class E1GoErmIFilesFileE1GoErmIURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


E1GoErmIFilesFile = Union[str, E1GoErmIFilesFileE1GoErmIURLAndHeaders]

PurgeCachZonePurgeParams = Union[E1GoErmIFlex, E1GoErmIEverything, E1GoErmIFiles]
