# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "AQxFrdVfFlex",
    "AQxFrdVfEverything",
    "AQxFrdVfFiles",
    "AQxFrdVfFilesFile",
    "AQxFrdVfFilesFileAQxFrdVfURLAndHeaders",
]


class AQxFrdVfFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class AQxFrdVfEverything(TypedDict, total=False):
    purge_everything: bool


class AQxFrdVfFiles(TypedDict, total=False):
    files: List[AQxFrdVfFilesFile]


class AQxFrdVfFilesFileAQxFrdVfURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


AQxFrdVfFilesFile = Union[str, AQxFrdVfFilesFileAQxFrdVfURLAndHeaders]

PurgeCachZonePurgeParams = Union[AQxFrdVfFlex, AQxFrdVfEverything, AQxFrdVfFiles]
