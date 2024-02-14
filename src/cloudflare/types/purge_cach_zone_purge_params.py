# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PurgeCachZonePurgeParams", "_2RAgAwD3Flex", "_2RAgAwD3Everything", "_2RAgAwD3Files", "2RAgAwD3FilesFile", "2RAgAwD3FilesFile_2RAgAwD3URLAndHeaders"]

class _2RAgAwD3Flex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]

class _2RAgAwD3Everything(TypedDict, total=False):
    purge_everything: bool

class _2RAgAwD3Files(TypedDict, total=False):
    files: List[2RAgAwD3FilesFile]

class 2RAgAwD3FilesFile_2RAgAwD3URLAndHeaders(TypedDict, total=False):
    headers: object

    url: str

2RAgAwD3FilesFile = Union[str, 2RAgAwD3FilesFile_2RAgAwD3URLAndHeaders]

PurgeCachZonePurgeParams = Union[_2RAgAwD3Flex, _2RAgAwD3Everything, _2RAgAwD3Files]