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
    "Y4HMkxYgFlex",
    "Y4HMkxYgEverything",
    "Y4HMkxYgFiles",
    "Y4HMkxYgFilesFile",
    "Y4HMkxYgFilesFileY4HMkxYgURLAndHeaders",
]


class Y4HMkxYgFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class Y4HMkxYgEverything(TypedDict, total=False):
    purge_everything: bool


class Y4HMkxYgFiles(TypedDict, total=False):
    files: List[Y4HMkxYgFilesFile]


class Y4HMkxYgFilesFileY4HMkxYgURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


Y4HMkxYgFilesFile = Union[str, Y4HMkxYgFilesFileY4HMkxYgURLAndHeaders]

PurgeCachZonePurgeParams = Union[Y4HMkxYgFlex, Y4HMkxYgEverything, Y4HMkxYgFiles]
