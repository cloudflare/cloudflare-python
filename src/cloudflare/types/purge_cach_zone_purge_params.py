# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PurgeCachZonePurgeParams", "_7mnXeLx2Flex", "_7mnXeLx2Everything", "_7mnXeLx2Files", "7mnXeLx2FilesFile", "7mnXeLx2FilesFile_7mnXeLx2URLAndHeaders"]

class _7mnXeLx2Flex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]

class _7mnXeLx2Everything(TypedDict, total=False):
    purge_everything: bool

class _7mnXeLx2Files(TypedDict, total=False):
    files: List[7mnXeLx2FilesFile]

class 7mnXeLx2FilesFile_7mnXeLx2URLAndHeaders(TypedDict, total=False):
    headers: object

    url: str

7mnXeLx2FilesFile = Union[str, 7mnXeLx2FilesFile_7mnXeLx2URLAndHeaders]

PurgeCachZonePurgeParams = Union[_7mnXeLx2Flex, _7mnXeLx2Everything, _7mnXeLx2Files]