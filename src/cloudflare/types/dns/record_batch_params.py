# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .record_param import RecordParam
from .batch_put_param import BatchPutParam
from .batch_patch_param import BatchPatchParam

__all__ = ["RecordBatchParams", "Delete"]


class RecordBatchParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    deletes: Iterable[Delete]

    patches: Iterable[BatchPatchParam]

    posts: Iterable[RecordParam]

    puts: Iterable[BatchPutParam]


class Delete(TypedDict, total=False):
    id: Required[str]
    """Identifier"""
