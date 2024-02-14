# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PurgeCachZonePurgeParams", "_42usXJnWFlex", "_42usXJnWEverything", "_42usXJnWFiles", "42usXJnWFilesFile", "42usXJnWFilesFile_42usXJnWURLAndHeaders"]

class _42usXJnWFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]

class _42usXJnWEverything(TypedDict, total=False):
    purge_everything: bool

class _42usXJnWFiles(TypedDict, total=False):
    files: List[42usXJnWFilesFile]

class 42usXJnWFilesFile_42usXJnWURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str

42usXJnWFilesFile = Union[str, 42usXJnWFilesFile_42usXJnWURLAndHeaders]

PurgeCachZonePurgeParams = Union[_42usXJnWFlex, _42usXJnWEverything, _42usXJnWFiles]