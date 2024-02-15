# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PurgeCachZonePurgeParams", "_2sq4ljBlFlex", "_2sq4ljBlEverything", "_2sq4ljBlFiles", "2sq4ljBlFilesFile", "2sq4ljBlFilesFile_2sq4ljBlURLAndHeaders"]

class _2sq4ljBlFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]

class _2sq4ljBlEverything(TypedDict, total=False):
    purge_everything: bool

class _2sq4ljBlFiles(TypedDict, total=False):
    files: List[2sq4ljBlFilesFile]

class 2sq4ljBlFilesFile_2sq4ljBlURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str

2sq4ljBlFilesFile = Union[str, 2sq4ljBlFilesFile_2sq4ljBlURLAndHeaders]

PurgeCachZonePurgeParams = Union[_2sq4ljBlFlex, _2sq4ljBlEverything, _2sq4ljBlFiles]