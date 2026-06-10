# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DataTagCategoryUpdateParams", "Tag"]


class DataTagCategoryUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    description: Optional[str]

    name: Optional[str]

    tags: Optional[Iterable[Tag]]
    """The desired final state of tags.

    - `None` (omitted): no tag changes.
    - `Some([])`: delete all tags.
    - `Some([...])`: desired final set + order.
    """


class Tag(TypedDict, total=False):
    id: Optional[str]
    """If `None` (omitted), a new tag will be created.

    Otherwise, an existing tag will be updated.
    """

    description: Optional[str]

    name: Optional[str]
