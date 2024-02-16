# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "GJq47JoyFlex",
    "GJq47JoyEverything",
    "GJq47JoyFiles",
    "GJq47JoyFilesFile",
    "GJq47JoyFilesFileGJq47JoyURLAndHeaders",
]


class GJq47JoyFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class GJq47JoyEverything(TypedDict, total=False):
    purge_everything: bool


class GJq47JoyFiles(TypedDict, total=False):
    files: List[GJq47JoyFilesFile]


class GJq47JoyFilesFileGJq47JoyURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


GJq47JoyFilesFile = Union[str, GJq47JoyFilesFileGJq47JoyURLAndHeaders]

PurgeCachZonePurgeParams = Union[GJq47JoyFlex, GJq47JoyEverything, GJq47JoyFiles]
