# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["TagCategoryUpdateParams"]


class TagCategoryUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    category_uuids: Required[SequenceNotStr[str]]
