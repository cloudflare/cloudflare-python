# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "VFc1B2WbFlex",
    "VFc1B2WbEverything",
    "VFc1B2WbFiles",
    "VFc1B2WbFilesFile",
    "VFc1B2WbFilesFileVFc1B2WbURLAndHeaders",
]


class VFc1B2WbFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class VFc1B2WbEverything(TypedDict, total=False):
    purge_everything: bool


class VFc1B2WbFiles(TypedDict, total=False):
    files: List[VFc1B2WbFilesFile]


class VFc1B2WbFilesFileVFc1B2WbURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


VFc1B2WbFilesFile = Union[str, VFc1B2WbFilesFileVFc1B2WbURLAndHeaders]

PurgeCachZonePurgeParams = Union[VFc1B2WbFlex, VFc1B2WbEverything, VFc1B2WbFiles]
