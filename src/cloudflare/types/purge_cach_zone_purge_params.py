# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PurgeCachZonePurgeParams", "_9XpUpQAxFlex", "_9XpUpQAxEverything", "_9XpUpQAxFiles", "9XpUpQAxFilesFile", "9XpUpQAxFilesFile_9XpUpQAxURLAndHeaders"]

class _9XpUpQAxFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]

class _9XpUpQAxEverything(TypedDict, total=False):
    purge_everything: bool

class _9XpUpQAxFiles(TypedDict, total=False):
    files: List[9XpUpQAxFilesFile]

class 9XpUpQAxFilesFile_9XpUpQAxURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str

9XpUpQAxFilesFile = Union[str, 9XpUpQAxFilesFile_9XpUpQAxURLAndHeaders]

PurgeCachZonePurgeParams = Union[_9XpUpQAxFlex, _9XpUpQAxEverything, _9XpUpQAxFiles]