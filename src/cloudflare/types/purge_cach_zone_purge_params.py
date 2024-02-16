# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PurgeCachZonePurgeParams", "_9HseNYt2Flex", "_9HseNYt2Everything", "_9HseNYt2Files", "9HseNYt2FilesFile", "9HseNYt2FilesFile_9HseNYt2URLAndHeaders"]

class _9HseNYt2Flex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]

class _9HseNYt2Everything(TypedDict, total=False):
    purge_everything: bool

class _9HseNYt2Files(TypedDict, total=False):
    files: List[9HseNYt2FilesFile]

class 9HseNYt2FilesFile_9HseNYt2URLAndHeaders(TypedDict, total=False):
    headers: object

    url: str

9HseNYt2FilesFile = Union[str, 9HseNYt2FilesFile_9HseNYt2URLAndHeaders]

PurgeCachZonePurgeParams = Union[_9HseNYt2Flex, _9HseNYt2Everything, _9HseNYt2Files]