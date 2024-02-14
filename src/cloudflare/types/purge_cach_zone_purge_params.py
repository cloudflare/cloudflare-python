# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "Kp8Uqy1uFlex",
    "Kp8Uqy1uEverything",
    "Kp8Uqy1uFiles",
    "Kp8Uqy1uFilesFile",
    "Kp8Uqy1uFilesFileKp8Uqy1uURLAndHeaders",
]


class Kp8Uqy1uFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class Kp8Uqy1uEverything(TypedDict, total=False):
    purge_everything: bool


class Kp8Uqy1uFiles(TypedDict, total=False):
    files: List[Kp8Uqy1uFilesFile]


class Kp8Uqy1uFilesFileKp8Uqy1uURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


Kp8Uqy1uFilesFile = Union[str, Kp8Uqy1uFilesFileKp8Uqy1uURLAndHeaders]

PurgeCachZonePurgeParams = Union[Kp8Uqy1uFlex, Kp8Uqy1uEverything, Kp8Uqy1uFiles]
