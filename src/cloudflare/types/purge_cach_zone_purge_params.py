# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "Hv5ypxlmFlex",
    "Hv5ypxlmEverything",
    "Hv5ypxlmFiles",
    "Hv5ypxlmFilesFile",
    "Hv5ypxlmFilesFileHv5ypxlmURLAndHeaders",
]


class Hv5ypxlmFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class Hv5ypxlmEverything(TypedDict, total=False):
    purge_everything: bool


class Hv5ypxlmFiles(TypedDict, total=False):
    files: List[Hv5ypxlmFilesFile]


class Hv5ypxlmFilesFileHv5ypxlmURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


Hv5ypxlmFilesFile = Union[str, Hv5ypxlmFilesFileHv5ypxlmURLAndHeaders]

PurgeCachZonePurgeParams = Union[Hv5ypxlmFlex, Hv5ypxlmEverything, Hv5ypxlmFiles]
