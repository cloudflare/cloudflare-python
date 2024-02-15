# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "ONoTspwWFlex",
    "ONoTspwWEverything",
    "ONoTspwWFiles",
    "ONoTspwWFilesFile",
    "ONoTspwWFilesFileONoTspwWURLAndHeaders",
]


class ONoTspwWFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class ONoTspwWEverything(TypedDict, total=False):
    purge_everything: bool


class ONoTspwWFiles(TypedDict, total=False):
    files: List[ONoTspwWFilesFile]


class ONoTspwWFilesFileONoTspwWURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


ONoTspwWFilesFile = Union[str, ONoTspwWFilesFileONoTspwWURLAndHeaders]

PurgeCachZonePurgeParams = Union[ONoTspwWFlex, ONoTspwWEverything, ONoTspwWFiles]
