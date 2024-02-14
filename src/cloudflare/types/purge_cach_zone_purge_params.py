# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "RCpiguQqFlex",
    "RCpiguQqEverything",
    "RCpiguQqFiles",
    "RCpiguQqFilesFile",
    "RCpiguQqFilesFileRCpiguQqURLAndHeaders",
]


class RCpiguQqFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class RCpiguQqEverything(TypedDict, total=False):
    purge_everything: bool


class RCpiguQqFiles(TypedDict, total=False):
    files: List[RCpiguQqFilesFile]


class RCpiguQqFilesFileRCpiguQqURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


RCpiguQqFilesFile = Union[str, RCpiguQqFilesFileRCpiguQqURLAndHeaders]

PurgeCachZonePurgeParams = Union[RCpiguQqFlex, RCpiguQqEverything, RCpiguQqFiles]
