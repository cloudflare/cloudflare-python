# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes, SequenceNotStr

__all__ = ["ToMarkdownTransformParams", "File"]


class ToMarkdownTransformParams(TypedDict, total=False):
    account_id: Required[str]

    file: Required[File]


class File(TypedDict, total=False):
    files: Required[SequenceNotStr[FileTypes]]
