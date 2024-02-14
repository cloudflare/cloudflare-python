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
    "Ttm0zLoGFlex",
    "Ttm0zLoGEverything",
    "Ttm0zLoGFiles",
    "Ttm0zLoGFilesFile",
    "Ttm0zLoGFilesFileTtm0zLoGURLAndHeaders",
]


class Ttm0zLoGFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class Ttm0zLoGEverything(TypedDict, total=False):
    purge_everything: bool


class Ttm0zLoGFiles(TypedDict, total=False):
    files: List[Ttm0zLoGFilesFile]


class Ttm0zLoGFilesFileTtm0zLoGURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


Ttm0zLoGFilesFile = Union[str, Ttm0zLoGFilesFileTtm0zLoGURLAndHeaders]

PurgeCachZonePurgeParams = Union[Ttm0zLoGFlex, Ttm0zLoGEverything, Ttm0zLoGFiles]
