# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = [
    "PurgeCachZonePurgeParams",
    "C1O0vQPqFlex",
    "C1O0vQPqEverything",
    "C1O0vQPqFiles",
    "C1O0vQPqFilesFile",
    "C1O0vQPqFilesFileC1O0vQPqURLAndHeaders",
]


class C1O0vQPqFlex(TypedDict, total=False):
    hosts: List[str]

    prefixes: List[str]

    tags: List[str]


class C1O0vQPqEverything(TypedDict, total=False):
    purge_everything: bool


class C1O0vQPqFiles(TypedDict, total=False):
    files: List[C1O0vQPqFilesFile]


class C1O0vQPqFilesFileC1O0vQPqURLAndHeaders(TypedDict, total=False):
    headers: object

    url: str


C1O0vQPqFilesFile = Union[str, C1O0vQPqFilesFileC1O0vQPqURLAndHeaders]

PurgeCachZonePurgeParams = Union[C1O0vQPqFlex, C1O0vQPqEverything, C1O0vQPqFiles]
