# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "HDwfmVgpFlex",
    "HDwfmVgpEverything",
    "HDwfmVgpFiles",
    "HDwfmVgpFilesFile",
    "HDwfmVgpFilesFileHDwfmVgpURLAndHeaders",
]


class HDwfmVgpFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class HDwfmVgpEverything(TypedDict, total=False):
    purge_everything: bool


class HDwfmVgpFiles(TypedDict, total=False):
    files: List[HDwfmVgpFilesFile]


class HDwfmVgpFilesFileHDwfmVgpURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


HDwfmVgpFilesFile = Union[str, HDwfmVgpFilesFileHDwfmVgpURLAndHeaders]

PurgeCachZonePurgeParams = Union[HDwfmVgpFlex, HDwfmVgpEverything, HDwfmVgpFiles]
