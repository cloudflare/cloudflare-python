# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = [
    "PurgeCachZonePurgeParams",
    "GNp7h9ZcFlex",
    "GNp7h9ZcEverything",
    "GNp7h9ZcFiles",
    "GNp7h9ZcFilesFile",
    "GNp7h9ZcFilesFileGNp7h9ZcURLAndHeaders",
]


class GNp7h9ZcFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class GNp7h9ZcEverything(TypedDict, total=False):
    purge_everything: bool


class GNp7h9ZcFiles(TypedDict, total=False):
    files: List[GNp7h9ZcFilesFile]


class GNp7h9ZcFilesFileGNp7h9ZcURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


GNp7h9ZcFilesFile = Union[str, GNp7h9ZcFilesFileGNp7h9ZcURLAndHeaders]

PurgeCachZonePurgeParams = Union[GNp7h9ZcFlex, GNp7h9ZcEverything, GNp7h9ZcFiles]
