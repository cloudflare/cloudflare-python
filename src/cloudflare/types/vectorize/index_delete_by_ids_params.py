# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["IndexDeleteByIDsParams"]


class IndexDeleteByIDsParams(TypedDict, total=False):
    account_id: str
    """Identifier"""

    ids: SequenceNotStr[str]
    """A list of vector identifiers to delete from the index indicated by the path."""
