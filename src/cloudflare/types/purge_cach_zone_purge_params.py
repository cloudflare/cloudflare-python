# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "DRGs8IacFlex",
    "DRGs8IacEverything",
    "DRGs8IacFiles",
    "DrGs8IacFilesFile",
    "DrGs8IacFilesFileDRGs8IacURLAndHeaders",
]


class DRGs8IacFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class DRGs8IacEverything(TypedDict, total=False):
    purge_everything: bool


class DRGs8IacFiles(TypedDict, total=False):
    files: List[DrGs8IacFilesFile]


class DrGs8IacFilesFileDRGs8IacURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


DrGs8IacFilesFile = Union[str, DrGs8IacFilesFileDRGs8IacURLAndHeaders]

PurgeCachZonePurgeParams = Union[DRGs8IacFlex, DRGs8IacEverything, DRGs8IacFiles]
