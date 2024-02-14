# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "A0Lwu6OoFlex",
    "A0Lwu6OoEverything",
    "A0Lwu6OoFiles",
    "A0Lwu6OoFilesFile",
    "A0Lwu6OoFilesFileA0Lwu6OoURLAndHeaders",
]


class A0Lwu6OoFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class A0Lwu6OoEverything(TypedDict, total=False):
    purge_everything: bool


class A0Lwu6OoFiles(TypedDict, total=False):
    files: List[A0Lwu6OoFilesFile]


class A0Lwu6OoFilesFileA0Lwu6OoURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


A0Lwu6OoFilesFile = Union[str, A0Lwu6OoFilesFileA0Lwu6OoURLAndHeaders]

PurgeCachZonePurgeParams = Union[A0Lwu6OoFlex, A0Lwu6OoEverything, A0Lwu6OoFiles]
