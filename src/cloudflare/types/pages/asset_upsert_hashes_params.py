# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AssetUpsertHashesParams"]


class AssetUpsertHashesParams(TypedDict, total=False):
    hashes: Required[SequenceNotStr[str]]
    """List of file content hashes to register in the asset store."""
