# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "XYr1bNe9Flex",
    "XYr1bNe9Everything",
    "XYr1bNe9Files",
    "XYr1bNe9FilesFile",
    "XYr1bNe9FilesFileXYr1bNe9URLAndHeaders",
]


class XYr1bNe9Flex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class XYr1bNe9Everything(TypedDict, total=False):
    purge_everything: bool


class XYr1bNe9Files(TypedDict, total=False):
    files: List[XYr1bNe9FilesFile]


class XYr1bNe9FilesFileXYr1bNe9URLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


XYr1bNe9FilesFile = Union[str, XYr1bNe9FilesFileXYr1bNe9URLAndHeaders]

PurgeCachZonePurgeParams = Union[XYr1bNe9Flex, XYr1bNe9Everything, XYr1bNe9Files]
